# 📖 Complete Commands Reference

## How to Use This Guide

This document lists all available commands you can use with the AI Personal Assistant. Try them by typing or saying them!

---

## 🎯 Command Categories

### 1. ⏰ TIME & DATE COMMANDS

#### Tell Current Time
```
Text: "What time is it?"
Text: "Tell me the time"
Text: "Current time"
Voice: "What time is it?" 🎤

Response: "The current time is 06:47 PM"
```

#### Tell Current Date
```
Text: "What's today's date?"
Text: "What date is it?"
Text: "Today's date"
Voice: "What's today?" 🎤

Response: "Today is Tuesday, November 25, 2025"
```

---

### 2. 📋 REMINDER COMMANDS

#### Set a Reminder (Text)
```
Text: "Remind me to buy groceries"
Text: "Remind me to call mom"
Text: "Set a reminder to exercise"

Response: "Reminder set: [your reminder]"
```

#### Set a Reminder (Voice)
```
Voice: "Remind me to take a break" 🎤
Voice: "Set reminder to finish report" 🎤

Response: Spoken confirmation + text display
```

#### Add Reminder via Panel
```
1. Scroll to "Reminders" panel on the right
2. Type reminder text in the input field
3. Click "Add" button
4. Reminder appears in the list
```

#### Delete a Reminder
```
1. Locate reminder in the list
2. Click the "✕" button next to it
3. Reminder is removed
```

#### View All Reminders
- All active reminders appear in the right panel
- Max display limited to panel height (scroll if needed)

---

### 3. 🧮 MATH & CALCULATION COMMANDS

#### Basic Arithmetic
```
Text: "Calculate 2+2"
Text: "Calculate 10 * 5"
Text: "Calculate 100 - 25"
Text: "Calculate 20 / 4"

Response: "The answer is [result]"
```

#### More Examples
```
Text: "What is 15 multiplied by 3?"
Text: "Solve 50 + 50"
Text: "How much is 100 divided by 5?"
Text: "Calculate 2^10" (or "2**10")

Response: Shows calculated answer
```

**Supported Operations:**
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Exponentiation: `**` or `^`
- Parentheses: `()`

**Examples:**
```
2+2                    → 4
10*5                   → 50
(10+5)*2              → 30
2**3                  → 8
100/4                 → 25
```

---

### 4. 🔍 SEARCH COMMANDS

#### Web Search Requests
```
Text: "Search for Python tutorials"
Text: "Search for machine learning"
Text: "Look up JavaScript"

Response: "Searching for: [topic]"
       "To get real results, you'll need to configure a search API"
```

**Note:** Search capability is prepared but requires API configuration (Google Custom Search, DuckDuckGo API, etc.)

---

### 5. 👋 GREETING & CONVERSATION

#### Greetings
```
Text/Voice: "Hello!"
Text/Voice: "Hi!"
Text/Voice: "Hey!"
Text/Voice: "What's up?"

Response: Friendly greeting response
          "Hello! I'm your personal AI assistant. How can I help you today?"
```

#### Get Help
```
Text/Voice: "Help"
Text/Voice: "What can you do?"
Text/Voice: "Available commands"
Text/Voice: "What are your capabilities?"

Response: Shows all available features and example commands
```

#### Say Goodbye
```
Text/Voice: "Goodbye"
Text/Voice: "Bye"
Text/Voice: "Exit"
Text/Voice: "See you"

Response: "Goodbye! Have a great day!"
```

---

## 🎤 VOICE COMMANDS vs TEXT COMMANDS

### Using Voice (🎤 Listen Button)
1. Click the blue "🎤 Listen" button
2. Status changes to "🎤 Listening..."
3. Speak your command clearly
4. Release when done (auto-stops)
5. Response appears automatically

**Tips for Best Results:**
- Speak clearly and at normal pace
- Reduce background noise
- Use short, simple phrases
- Try single sentences
- Check microphone is enabled in browser

### Using Text (Keyboard)
1. Click in the text input field
2. Type your command
3. Press Enter or click "Send" button
4. Response appears immediately

**Advantages:**
- Works without microphone
- Good for quiet environments
- More precise input
- Works offline (locally)

---

## 🔊 VOICE RESPONSES

### Enable Voice Response
- Click the "🔊 Speak" button (purple/green toggle)
- When enabled: Response will be spoken aloud
- When disabled: Only text is displayed

### Adjust Voice Settings
**Speech Rate (Speed):**
- Lower (50-100): Slow, clear speech
- Medium (150): Normal speech
- Higher (200-300): Fast speech

**Volume:**
- Adjust the slider from 0% (silent) to 100% (max)

**How to Adjust:**
1. Find the "⚙️ Settings" panel on the right
2. Use the "Speech Rate" slider
3. Use the "Volume" slider
4. Changes apply immediately

---

## 💬 CHAT INTERFACE

### Sending Messages
```
METHOD 1: Text Input
1. Type in the text field at bottom
2. Press Enter or click "Send"

METHOD 2: Voice Input
1. Click "🎤 Listen" button
2. Speak your command
3. Auto-processes your speech

METHOD 3: Keyboard Shortcut
1. Type anywhere (auto-focuses input)
2. Press Enter to send
```

### Reading Conversation
- Messages appear in the chat window
- Your messages: Right-aligned, blue background 👤
- Assistant messages: Left-aligned, light background 🤖
- Auto-scrolls to latest message
- Color-coded for easy reading

### Clear History
- Click "🗑️ Clear" button
- Removes all messages from display
- Chat is reset and ready for new conversation
- Backend history is also cleared

---

## ⚙️ ADVANCED FEATURES

### Conversation Context
- Previous messages are visible in chat
- Assistant maintains conversation flow
- Use pronouns in follow-up commands
- Example: "What time is it?" → "Remind me at that time"

### Quick Commands
```
Type these for instant responses:
- "help" → Shows all commands
- "time" → Current time
- "date" → Current date
- "goodbye" → Says goodbye
```

### Command Variations
Most commands accept multiple phrasings:

```
"What time is it?"     ✓
"Tell me the time"     ✓
"Current time?"        ✓
"Time?"                ✓

All do the same thing!
```

---

## 🐛 TROUBLESHOOTING COMMANDS

### If Voice Recognition Doesn't Work
```
Solution 1: Try Text Input
- Type instead of speaking
- Check microphone in browser settings

Solution 2: Check Permission
- Browser may ask for microphone permission
- Allow access when prompted
- Try refreshing the page

Solution 3: Check Backend
- Verify Flask backend is running
- Check browser console for errors (F12)
- See README.md troubleshooting section
```

### If Response is Not Correct
```
Example Problem: "What's 2+2" → Error response

Solution:
- Try rephrasing: "Calculate 2+2"
- Use exact format: "Calculate [expression]"
- Check backend console for errors
- Reload page and try again
```

### If Commands Not Recognized
```
Common Issues:
- Backend not running
- Connection error (check console)
- Typo in command
- Unsupported command

Solution:
1. Verify backend is running (http://localhost:5000)
2. Check browser console (F12 → Console tab)
3. Try a simpler command first (e.g., "Help")
4. See README.md for full troubleshooting
```

---

## 📝 COMMAND SYNTAX GUIDE

### Time Format
```
Output: HH:MM AM/PM
Example: "The current time is 06:47 PM"
```

### Date Format
```
Output: Day, Month Date, Year
Example: "Today is Tuesday, November 25, 2025"
```

### Math Expression Format
```
Valid: 2+2, 10*5, 100/4, 2**3, (10+5)*2
Invalid: "add 2 to 2", "multiply 10 by 5"
Use: "Calculate [expression]"
```

### Reminder Format
```
Input: "Remind me to [task]"
Storage: Plain text
Display: In reminders panel
```

---

## 🎓 LEARNING & TIPS

### Pro Tips
1. **Voice is fun**: Use voice input for hands-free operation
2. **Text is precise**: Type for exact math or complex queries
3. **Mix and match**: Use voice or text based on situation
4. **Clear reminders**: Delete old reminders to keep list clean
5. **Try variations**: Many command phrasings work

### Experiment
- Try different command phrasings
- Mix voice and text
- Test edge cases
- Share feedback!

### Keyboard Shortcuts
- **Enter** - Send text command
- **F12** - Open browser console (debugging)
- **Ctrl+L** - Focus address bar (to reload)

---

## 🔗 INTEGRATION OPTIONS

### Add New Commands (For Developers)
```python
# In backend/nlp_processor.py
self.intents['weather'] = ['what is the weather', 'how is it outside']

# In backend/handlers.py
def handle_weather(self, command_data):
    return {'response': 'Weather info...', 'data': None}
```

### Connect External APIs
```python
# In backend/handlers.py
import requests

def handle_news(self, command_data):
    response = requests.get('https://api.newsapi.org/...')
    return {'response': 'News...', 'data': news}
```

---

## 📚 QUICK REFERENCE TABLE

| Command | Type | Example | Response |
|---------|------|---------|----------|
| Time | Text/Voice | "What time is it?" | Current time |
| Date | Text/Voice | "What's today?" | Current date |
| Reminder | Text/Voice | "Remind me to..." | Confirmation |
| Math | Text | "Calculate 2+2" | Result |
| Search | Text | "Search for..." | Search query |
| Help | Text/Voice | "Help" | Help text |
| Greeting | Text/Voice | "Hello!" | Response |
| Goodbye | Text/Voice | "Goodbye" | Farewell |

---

## 🎉 QUICK START

1. **Type in the text field** or **click 🎤 Listen** for voice
2. **Press Enter** or **click Send**
3. **See the response** in the chat
4. **Enable 🔊 Speak** to hear responses
5. **Adjust settings** in the right panel

**Try these first:**
- "What time is it?"
- "Remind me to exercise"
- "Calculate 10 + 5"
- "Help"

---

**Last Updated**: November 25, 2025
**Status**: ✅ Ready to Use
**Version**: 1.0
