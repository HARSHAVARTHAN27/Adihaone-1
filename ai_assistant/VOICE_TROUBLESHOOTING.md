# 🔊 Audio/Voice Not Working - Troubleshooting Guide

## Quick Checklist

- [ ] System volume is ON (check Windows volume slider)
- [ ] Speakers/Headphones are connected and working
- [ ] Browser hasn't muted the tab (check browser audio icon)
- [ ] No other process is blocking audio
- [ ] pyttsx3 is properly installed

---

## Solution 1: Fix pyttsx3 on Windows (Recommended)

### Step 1: Install Required Dependencies

pyttsx3 on Windows uses SAPI (System Audio Processing Interface). You might need to reinstall it:

```powershell
cd c:\Users\Harshavardhan\Desktop\internship\ai-assistant
pip uninstall pyttsx3 -y
pip install pyttsx3 --upgrade
```

### Step 2: Test Text-to-Speech Directly

```powershell
cd c:\Users\Harshavardhan\Desktop\internship\ai-assistant\backend
python -c "
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
engine.say('Hello, this is a test')
engine.runAndWait()
print('Test complete')
"
```

If you **hear sound**, the issue is in the backend. If you **don't hear sound**, you need to:

### Step 3: Fix Windows Audio (If No Sound in Test)

1. **Check SAPI Installation:**
   - Open Settings → Sound → Volume
   - Make sure volume is not muted
   - Test with a YouTube video (verify speakers work)

2. **Reinstall pyttsx3 with SAPI:**
   ```powershell
   pip install pyttsx3 --force-reinstall
   ```

3. **Alternative: Use Windows Built-in TTS**
   ```powershell
   powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Hello World')"
   ```
   If this works, speakers are fine!

---

## Solution 2: Enable Browser Audio Output

The AI Assistant uses **Web Speech API** for browser-based audio:

1. **Check Browser Permissions:**
   - Chrome: Settings → Privacy → Microphone/Speaker
   - Firefox: about:preferences → Privacy & Security

2. **Test Browser Audio:**
   - Open: http://localhost:5000
   - Open Browser Console (F12)
   - Paste this code:
   ```javascript
   const utterance = new SpeechSynthesisUtterance('Hello, can you hear me?');
   window.speechSynthesis.speak(utterance);
   ```
   - Press Enter - you should hear "Hello, can you hear me?"

3. **If You Hear It:** Browser audio works! The issue is the backend.

---

## Solution 3: Enable Backend Audio Debugging

Edit `backend/app.py` and add debug output:

```python
def speak_response(text):
    """Speak the response in a separate thread."""
    try:
        if auto_speak_enabled:
            print(f"[DEBUG] Speaking: {text[:50]}...")
            tts.speak(text)
            print(f"[DEBUG] Spoke successfully")
    except Exception as e:
        print(f"[ERROR] Error speaking response: {e}")
```

Then check the terminal for messages when you send a message.

---

## Solution 4: Use Deepgram for High-Quality Audio

Deepgram has excellent text-to-speech. Update your `.env`:

```
API_PROVIDER=groq
FREE_API_KEY=your_groq_key
DEEPGRAM_API_KEY=your_deepgram_key
```

Then update `app.py` to use Deepgram TTS (premium quality audio).

---

## Solution 5: Check If Messages Are Being Processed

1. Open http://localhost:5000
2. Open Developer Tools (F12)
3. Go to Network tab
4. Type a message and send it
5. Look for the `/api/process_text` request
6. Check if it returns successfully (200 status)
7. Look for the response text in the response body

If requests are working but no audio, it's an audio playback issue.

---

## Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| "pyttsx3 not found" | `pip install pyttsx3` |
| No sound from speakers | Check Windows volume & speaker connections |
| Browser muted | Click speaker icon in address bar |
| pyttsx3 hangs/freezes | Install SAPI5 on Windows |
| Multiple voice issues | Restart browser and backend |

---

## Windows SAPI5 Installation (If All Else Fails)

1. Download: https://www.microsoft.com/en-us/download/details.aspx?id=10121
2. Install it
3. Restart your computer
4. Try again

---

## Test Commands

### Test 1: Direct Python Test
```powershell
python -c "import pyttsx3; engine = pyttsx3.init(); engine.say('Test'); engine.runAndWait()"
```

### Test 2: Browser Web Speech API
```javascript
// Open browser console (F12) and paste:
const u = new SpeechSynthesisUtterance('Testing');
speechSynthesis.speak(u);
```

### Test 3: Backend API Test
```powershell
curl -X POST http://localhost:5000/api/process_text -H "Content-Type: application/json" -d "{\"text\":\"Hello\"}"
```

---

## Need Help?

If you've tried all solutions and still no audio:

1. **Check if this works:** 
   - Windows Settings → Sound → Test speaker
   - Play a YouTube video

2. **If speakers work:** The issue is software (pyttsx3)
   - Try Solution 1 again with clean reinstall

3. **If speakers don't work:** Hardware issue
   - Check speaker connections
   - Update audio drivers
   - Try different speakers/headphones

---

## Alternative: Disable Auto-Voice & Use Text Only

If you want to disable automatic voice for now:

Edit `backend/app.py` line 44:
```python
auto_speak_enabled = False  # Change True to False
```

Restart backend. Now responses will be text-only (no voice).

You can still see the AI's responses - just won't be spoken.

---

## Quick Recovery Steps

```powershell
# 1. Stop the backend (Ctrl+C in terminal)
# 2. Clean reinstall
cd c:\Users\Harshavardhan\Desktop\internship\ai-assistant
pip uninstall pyttsx3 -y
pip install pyttsx3 --upgrade

# 3. Test directly
python -c "import pyttsx3; e = pyttsx3.init(); e.say('Test'); e.runAndWait()"

# 4. Restart backend
cd backend
python app.py
```

---

Let me know which step you'd like to try first! 🎙️
