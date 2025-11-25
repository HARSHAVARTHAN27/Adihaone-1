"""
Root-level Flask app entry point for Vercel deployment.
This is a minimal wrapper that Vercel can find and deploy.
"""
import os
import sys
import json
import threading

# Add ai_assistant/backend to path for imports
backend_path = os.path.join(os.path.dirname(__file__), 'ai_assistant', 'backend')
sys.path.insert(0, backend_path)

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# Try to import the backend modules
try:
    from free_api_processor import FreeAPIProcessor
    from text_to_speech import TextToSpeech
except ImportError as e:
    print(f"Warning: Could not import backend modules: {e}")
    FreeAPIProcessor = None
    TextToSpeech = None

# Try to import speech recognition, but don't fail if it's not available
try:
    from speech_recognition_module import SpeechRecognitionModule
    SPEECH_RECOGNITION_AVAILABLE = True
except (ImportError, ModuleNotFoundError) as e:
    print(f"Warning: Speech recognition not available: {e}")
    SPEECH_RECOGNITION_AVAILABLE = False
    SpeechRecognitionModule = None

# Load environment variables
load_dotenv()

# Get the path to frontend directory
frontend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ai_assistant', 'frontend')

# Initialize Flask app
app = Flask(__name__, static_folder=frontend_path, static_url_path='')
CORS(app)

# Initialize components
api_provider = os.getenv('API_PROVIDER', 'groq')
api_key = os.getenv('FREE_API_KEY', '')

api_processor = None
if FreeAPIProcessor:
    try:
        api_processor = FreeAPIProcessor(api_key=api_key, api_provider=api_provider)
    except ValueError as e:
        print(f"Warning: API not configured: {e}")

tts = None
if TextToSpeech:
    tts = TextToSpeech()

speech_recognizer = None
if SPEECH_RECOGNITION_AVAILABLE and SpeechRecognitionModule:
    speech_recognizer = SpeechRecognitionModule()

# Track conversation state
conversation_history = []
auto_speak_enabled = True
active_threads = []


def speak_response(text):
    """Speak the response in a separate thread."""
    try:
        if auto_speak_enabled and tts:
            text_preview = text[:50].replace('\n', ' ')
            print(f"🎤 Speaking: {text_preview}...", flush=True)
            tts.speak(text)
            print(f"✓ Speech completed", flush=True)
    except Exception as e:
        print(f"❌ Error speaking response: {e}", flush=True)


@app.route('/', methods=['GET'])
def serve_index():
    """Serve the main index.html file."""
    try:
        return send_from_directory(frontend_path, 'index.html')
    except:
        return "AI Assistant Backend Running", 200


@app.route('/<path:path>', methods=['GET'])
def serve_static(path):
    """Serve static files."""
    try:
        return send_from_directory(frontend_path, path)
    except:
        return jsonify({'error': 'Not found'}), 404


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint."""
    models = []
    status = 'ok'
    if api_processor:
        try:
            models = api_processor.get_available_models()
        except:
            pass
    
    return jsonify({
        'status': status,
        'message': 'AI Assistant is running',
        'provider': api_provider,
        'auto_speak': auto_speak_enabled,
        'available_models': models
    })


@app.route('/api/process_text', methods=['POST'])
def process_text():
    """Process text command using Free API."""
    try:
        if not api_processor:
            return jsonify({
                'error': 'API not configured',
                'response': 'Please configure your FREE_API_KEY in .env file'
            }), 503
        
        data = request.json
        user_text = data.get('text', '').strip()
        
        if not user_text:
            return jsonify({
                'error': 'No text provided',
                'response': 'Please provide some text.'
            }), 400
        
        result = api_processor.process(user_text)
        response_text = result.get('response', 'No response')
        
        conversation_history.append({
            'user': user_text,
            'assistant': response_text,
            'timestamp': len(conversation_history)
        })
        
        if tts:
            speak_thread = threading.Thread(target=speak_response, args=(response_text,))
            speak_thread.daemon = False
            speak_thread.start()
            active_threads.append(speak_thread)
            active_threads[:] = [t for t in active_threads if t.is_alive()]
        
        return jsonify({
            'response': response_text,
            'error': result.get('error', False),
            'provider': api_provider
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'response': 'An error occurred processing your request.'
        }), 500


@app.route('/api/speak_toggle', methods=['POST'])
def speak_toggle():
    """Toggle automatic voice response."""
    global auto_speak_enabled
    data = request.json or {}
    auto_speak_enabled = data.get('enabled', not auto_speak_enabled)
    
    return jsonify({
        'auto_speak_enabled': auto_speak_enabled,
        'message': 'Auto speak ' + ('enabled' if auto_speak_enabled else 'disabled')
    })


@app.route('/api/history', methods=['GET'])
def get_history():
    """Get conversation history."""
    limit = request.args.get('limit', 50, type=int)
    return jsonify({
        'history': conversation_history[-limit:],
        'total': len(conversation_history)
    })


@app.route('/api/clear_history', methods=['POST'])
def clear_history():
    """Clear conversation history."""
    global conversation_history
    conversation_history = []
    return jsonify({'status': 'ok', 'message': 'History cleared'})


@app.route('/api/models', methods=['GET'])
def get_models():
    """Get available models."""
    models = []
    if api_processor:
        try:
            models = api_processor.get_available_models()
        except:
            pass
    return jsonify({
        'models': models,
        'current_provider': api_provider
    })


if __name__ == '__main__':
    print("Starting AI Personal Assistant Backend...")
    print(f"Using API Provider: {api_provider}")
    app.run(debug=True, port=5000)

