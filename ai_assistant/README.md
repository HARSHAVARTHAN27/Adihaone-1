# 🤖 AI Personal Assistant

A voice-enabled AI personal assistant that responds to user commands through natural language processing. Built with Python Flask backend and modern web frontend.

## Features

✨ **Core Capabilities:**
- 🎤 **Speech-to-Text**: Convert voice commands to text using Web Speech API
- 🔊 **Text-to-Speech**: AI responds with natural-sounding voice
- ⏰ **Tell Time/Date**: Ask "What time is it?" or "What's today's date?"
- 📋 **Reminders**: Set and manage reminders
- 🔍 **Web Search**: Search for information (requires API configuration)
- 🧮 **Math Solver**: Calculate and solve math problems
- 💬 **Natural Language Processing**: Understands user intent and context

## Tech Stack

### Backend
- **Flask** - Python web framework
- **spaCy** - NLP processing (optional, for advanced text processing)
- **SpeechRecognition** - Audio processing
- **pyttsx3** - Text-to-speech synthesis
- **wolframalpha** - Math solving and knowledge queries
- **Flask-CORS** - Cross-origin resource sharing

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with animations
- **JavaScript (Vanilla)** - Web Speech API, Fetch API
- **Responsive Design** - Works on desktop and mobile

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Modern web browser (Chrome, Edge, Firefox recommended)

### Step 1: Clone and Navigate

```bash
cd c:\Users\Harshavardhan\Desktop\internship\ai-assistant
```

### Step 2: Create Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If you're on Linux/Mac:
```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: (Optional) Download spaCy Model

For more advanced NLP processing:
```bash
python -m spacy download en_core_web_sm
```

### Step 5: Configure Environment (Optional)

Create a `.env` file in the backend directory with optional API keys:

```bash
# .env file in backend/
WOLFRAM_APP_ID=your_wolfram_app_id_here
GOOGLE_API_KEY=your_google_api_key_here
```

**Getting API Keys:**
- **WolframAlpha**: Sign up at https://www.wolframalpha.com/api/
- **Google Custom Search**: Set up at https://cse.google.com/

## Running the Application

### Terminal 1: Start Backend Server

```bash
cd backend
python app.py
```

You should see:
```
Starting AI Personal Assistant Backend...
Server running on http://localhost:5000
```

### Terminal 2: Start Frontend

Simply open the frontend in a web browser:

**Option 1**: Open directly
```bash
# Navigate to the frontend folder and open index.html
cd frontend
start index.html
```

**Option 2**: Using a simple HTTP server
```powershell
cd frontend
python -m http.server 8000
```

Then open http://localhost:8000 in your browser.

## Usage

### Text Commands

1. Type a command in the text input box
2. Click "Send" or press Enter
3. The assistant will process and respond

### Voice Commands

1. Click the "🎤 Listen" button
2. Speak your command clearly
3. The assistant will transcribe and respond
4. Enable "🔊 Speak" to hear the response

### Example Commands

```
"What time is it?"
"What's today's date?"
"Remind me to buy groceries"
"Calculate 15 × 20"
"Search for Python tutorials"
"What's the weather?"
"Tell me a joke"
```

### Managing Reminders

- Add reminders using the side panel
- View all active reminders
- Click ✕ to delete a reminder

### Adjusting Settings

- **Speech Rate**: Adjust how fast the assistant speaks (50-300)
- **Volume**: Control speaker volume (0-100%)

## API Endpoints

### Chat Commands
```
POST /api/process_text
Body: { "text": "user command", "speak": true }
```

### Voice Input
```
POST /api/process_speech
Body: { "timeout": 10, "speak": true }
```

### Text-to-Speech
```
POST /api/tts
Body: { "text": "text to speak" }

POST /api/tts/settings
Body: { "rate": 150, "volume": 0.9 }
```

### Reminders
```
GET /api/reminders
POST /api/reminders
Body: { "text": "reminder text" }
DELETE /api/reminders/<id>
```

### Conversation History
```
GET /api/history
DELETE /api/history
```

### Health Check
```
GET /api/health
```

## Project Structure

```
ai-assistant/
├── backend/
│   ├── app.py                    # Flask app & API endpoints
│   ├── nlp_processor.py          # NLP intent recognition
│   ├── handlers.py               # Command handlers
│   ├── text_to_speech.py         # TTS functionality
│   └── speech_recognition_module.py  # STT functionality
├── frontend/
│   ├── index.html               # Main UI
│   ├── styles.css               # Styling
│   └── script.js                # Frontend logic
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Troubleshooting

### Backend won't start
- Ensure Python is installed: `python --version`
- Check virtual environment is activated
- Verify dependencies: `pip list`
- Check port 5000 is available: `netstat -ano | findstr :5000`

### Speech recognition not working
- Check microphone is connected and enabled
- Ensure browser has microphone permission
- Use Chrome, Edge, or Firefox (better compatibility)
- Check internet connection (uses Google's STT API)

### CORS errors
- Backend should be on http://localhost:5000
- Frontend should access `/api` endpoints via proxy or CORS headers
- Verify Flask-CORS is installed

### Speech-to-text not recognizing commands
- Speak clearly and at normal pace
- Reduce background noise
- Try shorter phrases
- Check microphone volume

## Advanced Features

### 1. Adding New Commands

Edit `backend/handlers.py` to add new command handlers:

```python
def handle_custom_command(self, command_data):
    return {
        'response': 'Your custom response',
        'data': None
    }
```

Update `backend/nlp_processor.py` to recognize the intent.

### 2. Integrating External APIs

Add API calls in `backend/handlers.py`:

```python
import requests

def handle_weather(self, command_data):
    response = requests.get('https://api.weather.com/...')
    # Process response
```

### 3. Database Integration

Add reminder persistence with SQLite or any database:

```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
```

### 4. Multi-language Support

Modify `frontend/script.js`:

```javascript
recognition.lang = 'es-ES'; // For Spanish
recognition.lang = 'fr-FR'; // For French
```

## Future Enhancements

- 🎯 Machine Learning model for intent recognition
- 🌍 Multi-language support
- 📱 Mobile app version
- 🔐 User authentication and profiles
- 💾 Database for persistent reminders
- 🎨 Theme customization
- 🧠 Conversational context memory
- 🔗 Integration with external APIs (weather, news, etc.)

## Dependencies

See `requirements.txt` for complete list:

- Flask==2.3.3
- flask-cors==4.0.0
- spacy==3.7.2
- SpeechRecognition==3.10.0
- pyttsx3==2.90
- wolframalpha==5.0.0
- requests==2.31.0
- python-dotenv==1.0.0

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions:
1. Check the Troubleshooting section
2. Review the code comments
3. Check backend console for error messages

## Contributing

Feel free to fork, modify, and improve this assistant!

Happy coding! 🚀
