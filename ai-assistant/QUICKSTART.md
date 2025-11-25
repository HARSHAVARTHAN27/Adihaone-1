# Quick Start Guide

## Installation Steps

1. **Open PowerShell and navigate to the project:**
   ```
   cd c:\Users\Harshavardhan\Desktop\internship\ai-assistant
   ```

2. **Create virtual environment:**
   ```
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Start the backend server (Terminal 1):**
   ```
   cd backend
   python app.py
   ```
   
   Expected output:
   ```
   Starting AI Personal Assistant Backend...
   Server running on http://localhost:5000
   ```

5. **Open frontend (Terminal 2 or Browser):**
   ```
   cd frontend
   start index.html
   ```
   
   Or open the file directly: `c:\Users\Harshavardhan\Desktop\internship\ai-assistant\frontend\index.html`

## Try These Commands

Once running, try these voice or text commands:

- "What time is it?"
- "What's today's date?"
- "Remind me to take a break"
- "Calculate 2+2"
- "Help"

## Keyboard Shortcuts

- **Enter**: Send text command
- **Click 🎤 Listen**: Start voice input
- **Click 🔊 Speak**: Toggle voice responses
- **Click 🗑️ Clear**: Clear chat history

## Need Help?

Check the README.md file for:
- Detailed feature list
- API endpoint documentation
- Troubleshooting guide
- Advanced configuration
