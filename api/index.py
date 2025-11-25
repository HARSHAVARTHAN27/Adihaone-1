"""
Vercel Serverless Function for AI Personal Assistant Flask App.
This file exports a 'handler' function for Vercel's Python runtime.
"""
import os
import sys
import json
import threading

# ----------------------------------------------------------------------------
# PATH CORRECTION for dependent modules
# ----------------------------------------------------------------------------
# Add the 'ai_assistant/backend' directory to the system path
# so that it can find the other Python modules like free_api_processor.
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ai_assistant', 'backend'))
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)
# ----------------------------------------------------------------------------

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# --- The rest of your application code ---

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
# Note: The path is now relative to the root of the project, not the api/ folder
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ai_assistant', 'frontend'))

# Initialize Flask app with static folder configuration
app = Flask(__name__, static_folder=frontend_path, static_url_path='')
CORS(app)

# Initialize components
api_provider = os.getenv('API_PROVIDER', 'groq')
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
auto_speak_enabled = True
active_threads = []


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
        
        result = api_processor.process(user_text)
        response_text = result.get('response', 'Error: No response from API.')
        
        conversation_history.append({
            'user': user_text,
            'assistant': response_text,
        })
        
        speak_thread = threading.Thread(target=speak_response, args=(response_text,))
        speak_thread.daemon = False
        speak_thread.start()
        
        return jsonify({
            'response': response_text,
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'response': 'An error occurred processing your request.'
        }), 500

# Add this line to export the WSGI application for Vercel
from vercel_wsgi import VercelWSGI

handler = VercelWSGI(app)
