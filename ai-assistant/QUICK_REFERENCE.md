# 🚀 QUICK START - Copy & Paste Commands

## Prerequisites Check
```powershell
# Check Python
python --version

# Check if venv exists
ls "c:\Users\Harshavardhan\Desktop\internship\ai-assistant\venv"
```

## STEP 1: Install Ollama

❌ **If not installed yet:**
- Visit: https://ollama.ai
- Download Windows installer
- Run installer
- Restart terminal

✅ **Verify installation:**
```powershell
ollama --version
```

## STEP 2: Download a Model (First Time Only)

```powershell
# Fast (recommended for first time)
ollama pull mistral

# Or larger model
ollama pull llama2

# Or chat-optimized
ollama pull neural-chat
```

⏱️ First time: ~5-10 minutes depending on internet speed

## STEP 3: Start Ollama (Terminal #1)

Keep this running while using the assistant:

```powershell
ollama serve
```

✅ You should see: `listening on 127.0.0.1:11434`

**Do NOT close this terminal!**

## STEP 4: Start AI Assistant (Terminal #2)

Open a NEW terminal/PowerShell window:

```powershell
cd "c:\Users\Harshavardhan\Desktop\internship\ai-assistant"
.\start-assistant.ps1
```

Or manually:
```powershell
cd "c:\Users\Harshavardhan\Desktop\internship\ai-assistant"
.\venv\Scripts\Activate.ps1
cd backend
python app.py
```

✅ You should see: `Running on http://127.0.0.1:5000`

**Keep this running!**

## STEP 5: Open Browser (Terminal #3 or same as #2 after app starts)

```
http://localhost:5000
```

Or click: http://localhost:5000

## ✨ That's It!

You should now see:
- 🎨 Beautiful modern UI
- 🤖 AI Assistant interface
- 🎤 Microphone button
- ⚙️ Settings button
- 📊 Connection status

## 🎯 Quick Usage

| Action | How |
|--------|-----|
| **Ask question** | Type in box + press Enter |
| **Speak command** | Click 🎤 button, speak clearly |
| **Auto voice** | Enabled by default, responses spoken |
| **Dark mode** | Click 🌙 button |
| **Settings** | Click ⚙️ button |
| **Change model** | In ⚙️ Settings dropdown |
| **Adjust volume** | Sidebar slider |
| **Adjust speed** | Sidebar slider |
| **View history** | Sidebar shows recent commands |
| **Clear history** | Click "Clear" in sidebar |

## 🔧 Troubleshooting

### "ollama is not recognized"
```powershell
# Restart terminal
# If still fails, add to PATH (see INSTALL_OLLAMA.md)
```

### "Cannot connect to Ollama"
```powershell
# Make sure you ran: ollama serve
# In a DIFFERENT terminal
```

### "Port 5000 already in use"
```powershell
# Kill the process using port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### "No sound"
- Check Windows volume (bottom right)
- Check browser permissions (F12 → Privacy)
- Check speaker is connected

## 📋 Files to Check

- `INSTALL_OLLAMA.md` - Detailed installation help
- `QUICKSTART_OLLAMA.md` - 5-minute setup
- `README_OLLAMA.md` - Full documentation
- `SETUP_SUMMARY.md` - Complete guide

## 🆘 Still Having Issues?

1. Open terminal and check:
   ```powershell
   ollama --version
   ```

2. In another terminal, test backend:
   ```powershell
   cd "c:\Users\Harshavardhan\Desktop\internship\ai-assistant\backend"
   .\..venv\Scripts\python.exe -c "import flask; print('Flask OK')"
   ```

3. Check browser console (F12 → Console tab) for errors

4. Read error messages carefully - they usually tell you what's wrong!

## 📞 Support

All documentation files have detailed troubleshooting sections.

---

## 🎉 Ready? Let's Go!

**Terminal 1:**
```powershell
ollama serve
```

**Terminal 2:**
```powershell
cd "c:\Users\Harshavardhan\Desktop\internship\ai-assistant"
.\start-assistant.ps1
```

**Browser:**
```
http://localhost:5000
```

**Enjoy!** 🤖✨
