"""
Flask backend for AI Personal Assistant with Free API integration.
"""
import os
import json
import threading
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

from free_api_processor import FreeAPIProcessor
from text_to_speech import TextToSpeech

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
frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend')

# Initialize Flask app with static folder configuration (only once)
app = Flask(__name__, static_folder=frontend_path, static_url_path='')
CORS(app)

# Initialize components
api_provider = os.getenv('API_PROVIDER', 'groq')  # Options: groq, huggingface, together
api_key = os.getenv('FREE_API_KEY', '')

try:
    api_processor = FreeAPIProcessor(api_key=api_key, api_provider=api_provider)
except ValueError as e:
    print(f"Warning: API not configured: {e}")
    api_processor = None

tts = TextToSpeech()
speech_recognizer = SpeechRecognitionModule() if SPEECH_RECOGNITION_AVAILABLE else None

# Track conversation state
conversation_history = []
auto_speak_enabled = True  # Enable automatic voice response by default
active_threads = []  # Track active speech threads


def speak_response(text):
    """Speak the response in a separate thread."""
    try:
        if auto_speak_enabled:
            text_preview = text[:50].replace('\n', ' ')
            print(f"🎤 Speaking: {text_preview}...", flush=True)
            tts.speak(text)
            print(f"✓ Speech completed", flush=True)
    except Exception as e:
        print(f"❌ Error speaking response: {e}", flush=True)


@app.route('/', methods=['GET'])
def serve_index():
    """Serve the main index.html file."""
    return send_from_directory(frontend_path, 'index.html')


@app.route('/<path:path>', methods=['GET'])
def serve_static(path):
    """Serve static files."""
    return send_from_directory(frontend_path, path)


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint."""
    if api_processor:
        models = api_processor.get_available_models()
        status = 'ok'
    else:
        models = []
        status = 'error'
    
    return jsonify({
        'status': status,
        'message': 'AI Assistant is running',
        'provider': api_provider,
        'auto_speak': auto_speak_enabled,
        'available_models': models
    })


@app.route('/api/process_text', methods=['POST'])
def process_text():
    """
    Process text command using Free API.
    
    Expected JSON:
    {
        "text": "user input text"
    }
    """
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
        
        # Process with Free API
        result = api_processor.process(user_text)
        
        if result.get('error'):
            response_text = result['response']
        else:
            response_text = result['response']
        
        # Add to conversation history
        conversation_history.append({
            'user': user_text,
            'assistant': response_text,
            'timestamp': len(conversation_history)
        })
        
        # Speak response in background thread (non-daemon so it completes)
        speak_thread = threading.Thread(target=speak_response, args=(response_text,))
        speak_thread.daemon = False
        speak_thread.start()
        active_threads.append(speak_thread)
        
        # Clean up finished threads
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


@app.route('/api/process_speech', methods=['POST'])
def process_speech():
    """
    Process speech input using microphone.
    
    Expected JSON:
    {
        "timeout": 10  # optional
    }
    """
    try:
        if not SPEECH_RECOGNITION_AVAILABLE:
            return jsonify({
                'error': 'Speech recognition not available',
                'response': 'Speech recognition is not configured. Please use text input instead.'
            }), 503
        
        data = request.json or {}
        timeout = data.get('timeout', 10)
        
        # Listen to speech
        recognized_text = speech_recognizer.listen(timeout=timeout)
        
        if not recognized_text:
            return jsonify({
                'error': 'No speech recognized',
                'response': 'I did not hear anything. Please try again.'
            }), 400
        
        # Process the recognized text
        result = api_processor.process(recognized_text)
        response_text = result['response']
        
        # Add to conversation history
        conversation_history.append({
            'user': recognized_text,
            'assistant': response_text,
            'timestamp': len(conversation_history)
        })
        
        # Speak response in background thread (non-daemon so it completes)
        speak_thread = threading.Thread(target=speak_response, args=(response_text,))
        speak_thread.daemon = False
        speak_thread.start()
        active_threads.append(speak_thread)
        
        # Clean up finished threads
        active_threads[:] = [t for t in active_threads if t.is_alive()]
        
        return jsonify({
            'user_input': recognized_text,
            'response': response_text,
            'error': result.get('error', False)
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'response': 'An error occurred processing your speech.'
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


@app.route('/api/tts/settings', methods=['POST'])
def tts_settings():
    """Update TTS settings."""
    try:
        data = request.json or {}
        
        if 'rate' in data:
            tts.set_rate(int(data['rate']))
        
        if 'volume' in data:
            tts.set_volume(float(data['volume']))
        
        if 'voice_index' in data:
            voice_idx = int(data['voice_index'])
            print(f"Setting voice to index: {voice_idx}", flush=True)
            tts.set_voice(voice_idx)
        
        return jsonify({'status': 'ok', 'message': 'TTS settings updated'})
    
    except Exception as e:
        print(f"Error in tts_settings: {e}", flush=True)
        return jsonify({'error': str(e)}), 500


@app.route('/api/tts/voices', methods=['GET'])
def get_voices():
    """Get available TTS voices."""
    try:
        voices = tts.get_available_voices()
        return jsonify({
            'voices': voices,
            'count': len(voices)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


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
    if api_processor:
        models = api_processor.get_available_models()
    else:
        models = []
    return jsonify({
        'models': models,
        'current_provider': api_provider
    })


@app.route('/api/model/set', methods=['POST'])
def set_model():
    """Set the model to use."""
    data = request.json or {}
    model = data.get('model', '')
    
    if api_processor and model:
        api_processor.set_model(model)
    
    return jsonify({
        'current_provider': api_provider,
        'message': f'Using {api_provider} provider'
    })


@app.route('/api/test/speak', methods=['POST'])
def test_speak():
    """Test endpoint to verify voice is working."""
    try:
        data = request.json or {}
        text = data.get('text', 'Hello, this is a test message!')
        voice_idx = int(data.get('voice_index', 0))
        
        print(f"Testing voice {voice_idx}: {text}", flush=True)
        tts.set_voice(voice_idx)
        
        # Speak in background thread
        speak_thread = threading.Thread(target=tts.speak, args=(text,))
        speak_thread.daemon = False
        speak_thread.start()
        
        return jsonify({
            'status': 'speaking',
            'text': text,
            'voice_index': voice_idx,
            'message': 'Test speech started'
        })
    except Exception as e:
        print(f"Error in test_speak: {e}", flush=True)
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    print("Starting AI Personal Assistant Backend with Free APIs...")
    print(f"Using API Provider: {api_provider}")
    print(f"Auto-speak enabled: {auto_speak_enabled}")
    print("Server running on http://localhost:5000")
    app.run(debug=True, port=5000)
