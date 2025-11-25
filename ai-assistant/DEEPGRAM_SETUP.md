# 🎙️ Deepgram Integration Guide

Deepgram is an excellent free API provider with specialized support for voice and audio processing.

## Why Deepgram?

- **50,000 free API calls per month** (highest free tier!)
- **Excellent speech-to-text** (STT) quality
- **Beautiful text-to-speech** (TTS) with multiple voices
- **Real-time processing** support
- **Affordable paid tier** if you exceed free quota
- **Developer-friendly** documentation

---

## Get Your Deepgram API Key

### Step 1: Sign Up
1. Go to: https://console.deepgram.com
2. Click **"Sign Up"** (free account)
3. No credit card required for free tier

### Step 2: Create API Key
1. Log in to your Deepgram account
2. Go to **Settings** → **API Keys**
3. Click **"Create New Key"**
4. Name it something like "AI Assistant"
5. Click **"Create"**
6. **Copy the API key** (starts with something like `8a7f...`)

### Step 3: Configure Your Assistant
Create or edit `.env` file in the backend folder:

```env
# Option A: Use Deepgram for both speech and LLM
API_PROVIDER=deepgram
DEEPGRAM_API_KEY=your_deepgram_key_here

# Option B: Use Deepgram for speech only, another provider for LLM
API_PROVIDER=groq
FREE_API_KEY=your_groq_key_here
DEEPGRAM_API_KEY=your_deepgram_key_here
```

---

## Deepgram Features

### Speech-to-Text (STT)
- Converts spoken audio to text
- Multiple language support
- Real-time transcription
- Excellent accuracy with various accents

### Text-to-Speech (TTS)
Available voices:
- **Female**: Asteria, Luna, Stella, Athena, Hera
- **Male**: Orion, Arcas, Perseus, Angus

### Features
- Natural-sounding voices
- Adjustable speaking rate
- Multiple languages
- SSML support for advanced control

---

## Setup Steps

### 1. Get API Key
Follow steps above to get your Deepgram API key.

### 2. Install Dependencies
```powershell
cd c:\Users\Harshavardhan\Desktop\internship\ai-assistant
pip install -r requirements.txt
```

### 3. Configure .env
Update `.env` in the backend folder with your API key.

### 4. Start Backend
```powershell
cd backend
python app.py
```

### 5. Test
Open http://localhost:5000 and start chatting!

---

## 📊 Free Tier Limits

| Service | Free Quota | Cost After |
|---------|-----------|-----------|
| **STT (Speech-to-Text)** | 50,000 requests/month | $0.0043 per request |
| **TTS (Text-to-Speech)** | 50,000 requests/month | $0.0059 per request |
| **Concurrent Streams** | 2 | Upgradeable |

That's approximately:
- ✅ **1,667 minutes of speech processing per month**
- ✅ **Completely free for personal use**
- ✅ **Generous for a small AI assistant**

---

## Troubleshooting

### "Invalid API Key" Error?
1. Check the key is copied correctly (no extra spaces)
2. Wait a few seconds after creating the key
3. Verify you're using a **free tier key** (not paid)
4. Try recreating the key

### Slow Responses?
- Deepgram is fast (usually < 100ms)
- Check your internet connection
- Ensure you're within free tier limits

### Need More Requests?
- Upgrade to paid tier (very affordable)
- Use multiple API keys (rotate them)
- Combine with another provider (Groq for LLM, Deepgram for voice)

---

## Combining with Other Providers

### Best Setup (Maximum Free Tier)
```env
# Deepgram for voice (50K free calls/month)
DEEPGRAM_API_KEY=your_deepgram_key

# Groq for LLM text generation (10K free calls/day)
API_PROVIDER=groq
FREE_API_KEY=your_groq_key
```

This gives you:
- ✅ Powerful text generation (Groq)
- ✅ Professional voice processing (Deepgram)
- ✅ Completely free
- ✅ 50K API calls from each service

---

## Features You Can Build

With Deepgram integration, you can:
- 🎤 Real-time speech recognition
- 🔊 High-quality voice responses
- 🌍 Multi-language support
- 📊 Transcription with confidence scores
- 🎯 Custom vocabulary and keywords
- 🎚️ Audio enhancement and diarization

---

## Next Steps

1. **Sign up** at https://console.deepgram.com
2. **Create an API key**
3. **Update .env** with your key
4. **Restart the backend**
5. **Test your AI Assistant**

Your AI Assistant now has professional-grade voice capabilities! 🚀

---

## Quick Links

- **Deepgram Console**: https://console.deepgram.com
- **Documentation**: https://developers.deepgram.com
- **API Reference**: https://developers.deepgram.com/reference
- **Pricing**: https://deepgram.com/pricing
- **Community**: https://github.com/deepgram-devs

---

## Questions?

- Check Deepgram documentation: https://developers.deepgram.com
- View API examples: https://github.com/deepgram-devs
- Contact Deepgram support through console

Enjoy your AI Assistant with professional voice capabilities! 🎉
