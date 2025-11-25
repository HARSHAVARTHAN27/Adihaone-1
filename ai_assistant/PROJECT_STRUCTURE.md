# 📁 Project Structure

```
ai-assistant/
│
├── 📄 README.md                          # Full documentation & API reference
├── 📄 QUICKSTART.md                      # Quick setup guide
├── 📄 requirements.txt                   # Python dependencies
│
├── 📁 backend/                           # Flask API Server
│   ├── 🐍 app.py                         # Main Flask application & endpoints
│   ├── 🐍 nlp_processor.py               # Natural Language Processing
│   ├── 🐍 handlers.py                    # Command handlers (time, math, etc)
│   ├── 🐍 text_to_speech.py              # TTS using pyttsx3
│   ├── 🐍 speech_recognition_module.py   # STT using speech_recognition
│   ├── 🐍 test_components.py             # Unit tests
│   └── 📄 .env.example                   # Environment variables template
│
└── 📁 frontend/                          # Web Interface
    ├── 🌐 index.html                     # Chat UI
    ├── 🎨 styles.css                     # Styling with animations
    └── ⚙️ script.js                      # Frontend logic & APIs
```

## Component Breakdown

### Backend Modules

| File | Purpose | Key Functions |
|------|---------|---------------|
| `app.py` | Flask REST API Server | `/api/process_text`, `/api/process_speech`, `/api/tts`, `/api/reminders` |
| `nlp_processor.py` | Intent Recognition & NLP | `recognize_intent()`, `extract_entities()`, `parse_command()` |
| `handlers.py` | Command Processing | `handle_time()`, `handle_reminder()`, `handle_math()`, `handle_search()` |
| `text_to_speech.py` | Voice Output | `speak()`, `set_rate()`, `set_volume()` |
| `speech_recognition_module.py` | Voice Input | `listen()`, `listen_from_file()` |
| `test_components.py` | Unit Tests | Test all components individually |

### Frontend Components

| File | Purpose | Features |
|------|---------|----------|
| `index.html` | Chat Interface | Message display, input controls, reminders panel |
| `styles.css` | Responsive Design | Animations, gradients, mobile-friendly layout |
| `script.js` | Client Logic | API calls, speech recognition, event handlers |

## API Endpoints

### Health & Core
- `GET /api/health` - Server status
- `POST /api/process_text` - Process text commands
- `POST /api/process_speech` - Process voice input

### Text-to-Speech
- `POST /api/tts` - Speak text
- `POST /api/tts/settings` - Configure speech rate/volume

### Reminders
- `GET /api/reminders` - List all reminders
- `POST /api/reminders` - Create reminder
- `DELETE /api/reminders/<id>` - Delete reminder

### History
- `GET /api/history` - Get conversation history
- `DELETE /api/history` - Clear history

## Key Features Implemented

✅ **NLP Module**
- Intent recognition (time, date, reminder, search, math, greeting, help, goodbye)
- Entity extraction (numbers, dates, time expressions)
- Keyword-based pattern matching
- Extensible intent system

✅ **Command Handlers**
- Time & date queries
- Reminder management
- Math problem solving
- Web search capability
- Natural language responses

✅ **Frontend UI**
- Clean, modern chat interface
- Text input with send button
- Voice input/output controls
- Reminder management panel
- TTS settings (rate & volume)
- Conversation history
- Responsive design

✅ **Integration**
- CORS enabled for cross-origin requests
- Structured JSON API responses
- Error handling
- Session state management

## Dependencies

### Python Packages
```
Flask==2.3.3           # Web framework
flask-cors==4.0.0      # Cross-origin support
SpeechRecognition==3.10.0  # Voice-to-text
pyttsx3==2.90          # Text-to-speech
wolframalpha==5.0.0    # Math & knowledge engine
requests==2.31.0       # HTTP requests
python-dotenv==1.0.0   # Environment variables
spacy==3.7.2           # NLP (optional)
```

### Browser APIs Used
- Web Speech API (speech recognition & synthesis)
- Fetch API (HTTP requests)
- LocalStorage (if extended)

## Running the Application

### 1. Setup
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Start Backend
```powershell
cd backend
python app.py
# Running on http://localhost:5000
```

### 3. Start Frontend
```powershell
cd frontend
start index.html
# Or use any HTTP server: python -m http.server 8000
```

### 4. Use the Assistant
- Type commands or click 🎤 to use voice
- Enable 🔊 for voice responses
- Manage reminders in the side panel
- Adjust speech settings as needed

## Testing

Run the test suite to verify all components:
```bash
cd backend
python test_components.py
```

Expected output: ✅ All tests completed successfully!

## Extension Points

### Add New Intents
Edit `backend/nlp_processor.py` - Add keywords to `self.intents` dict

### Add New Handlers
Edit `backend/handlers.py` - Add new `handle_*()` method and register in `process_command()`

### Customize Frontend
Edit `frontend/styles.css` - Modify colors, layout, animations
Edit `frontend/script.js` - Add new UI controls or API features

### Integrate APIs
Add to `backend/handlers.py`:
```python
def handle_weather(self, command_data):
    response = requests.get('https://api.weather.com/...')
    return {'response': 'Weather data...', 'data': data}
```

## Performance Notes

- Frontend uses vanilla JavaScript (no frameworks = fast loading)
- Backend uses Flask development server (suitable for local use)
- NLP uses simple keyword matching (fast, easily extensible)
- Optional spaCy support for advanced NLP
- Speech recognition uses Google's free API

## Security Considerations

- Running locally on localhost:5000
- No authentication (add if deploying)
- No database persistence (in-memory reminders)
- CORS enabled (restrict as needed)
- Input validation on backend

## Next Steps to Enhance

1. Add database persistence (SQLite/PostgreSQL)
2. Implement user authentication
3. Add more advanced NLP with machine learning
4. Integrate weather, news, calendar APIs
5. Add dark mode and theme customization
6. Create mobile app version
7. Deploy to cloud (Heroku, Azure, AWS)
8. Add multi-language support

---

**Status**: ✅ Fully Functional & Tested
**Last Updated**: November 25, 2025
