# 🚀 Free API Setup Guide

Your AI Assistant now uses **free APIs** instead of Ollama! Choose one of the following:

## Option 1: Groq (Recommended - Fastest & Most Free Tier)

### Get API Key
1. Go to: https://console.groq.com/keys
2. Sign up (free account)
3. Create a new API key
4. Copy the key

### Setup
1. Create `.env` file in the project root:
```
API_PROVIDER=groq
FREE_API_KEY=gsk_your_key_here
```

### Features
- **10,000 requests/day** (free tier)
- Ultra-fast responses (10-50ms)
- No credit card required for free tier
- Models: Mixtral, Llama, Gemma

---

## Option 2: Hugging Face

### Get API Key
1. Go to: https://huggingface.co/settings/tokens
2. Sign up (free account)
3. Create a new read-only token
4. Copy the token

### Setup
1. Create `.env` file:
```
API_PROVIDER=huggingface
FREE_API_KEY=hf_your_token_here
```

### Features
- Unlimited free tier (with rate limits)
- Great for learning and experimentation
- Multiple model options
- Community-driven

---

## Option 3: Together AI

### Get API Key
1. Go to: https://www.together.ai/signin
2. Sign up (free account)
3. You get **$5 free credit**
4. Navigate to API keys and copy yours

### Setup
1. Create `.env` file:
```
API_PROVIDER=together
FREE_API_KEY=b1a2c3d4e5f6_your_key_here
```

### Features
- $5 free credit (usually lasts ~500-1000 requests)
- Fast responses
- Premium models available
- Great documentation

---

## Quick Start

### 1. Choose Your Provider
Pick one of the options above and get your free API key.

### 2. Set Environment Variables
Create a `.env` file in the project root:
```
API_PROVIDER=groq
FREE_API_KEY=your_key_here
```

### 3. Install Dependencies
```powershell
cd c:\Users\Harshavardhan\Desktop\internship\ai-assistant
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 4. Start the Backend
```powershell
cd backend
python app.py
```

### 5. Open in Browser
Go to: http://localhost:5000

---

## 🎯 Pricing Comparison

| Provider | Free Tier | Speed | Quality |
|----------|-----------|-------|---------|
| **Groq** | 10K requests/day | ⚡⚡⚡ Fastest | ⭐⭐⭐⭐ Excellent |
| **Hugging Face** | Unlimited* | ⚡⚡ Good | ⭐⭐⭐ Good |
| **Together AI** | $5 free credit | ⚡⚡ Good | ⭐⭐⭐⭐⭐ Excellent |

*Hugging Face has rate limits but they're generous for free tier

---

## ⚠️ Troubleshooting

### "API not configured" Error?
- Check `.env` file exists with `FREE_API_KEY` set
- Verify API key is correct (copy-paste from provider)
- Restart the backend after changing `.env`

### "401 Unauthorized" Error?
- Invalid API key - double-check it's correct
- Some APIs require account verification via email
- Try a different API provider

### Slow Responses?
- Switch to Groq for fastest responses
- Check your internet connection
- Free tier has rate limits - wait a moment and retry

### "Rate Limited" Error?
- You've hit the free tier limit
- Wait a moment and try again
- Consider upgrading to paid tier or switching providers

---

## 📊 System Requirements

- **Internet**: Required (cloud-based APIs)
- **RAM**: 2GB minimum (much less than Ollama!)
- **Storage**: ~10MB for application files
- **No GPU needed**: All processing in cloud

---

## 💡 Pro Tips

1. **Groq for Best Free Experience**: 10K requests/day is very generous
2. **Combine Multiple APIs**: You can use different APIs for different needs
3. **Cost Monitoring**: Free tiers are sufficient for personal use
4. **API Status**: Check provider status if experiencing issues

---

## 🔗 Useful Links

- **Groq Console**: https://console.groq.com
- **Hugging Face Tokens**: https://huggingface.co/settings/tokens
- **Together AI Dashboard**: https://www.together.ai
- **API Documentation**: See each provider's docs for advanced features

---

## ✅ Success Indicators

After setup, you should see:
- ✅ Backend running on http://127.0.0.1:5000
- ✅ Frontend loads with beautiful UI
- ✅ Voice recognition working
- ✅ AI responses appearing in chat
- ✅ Text-to-speech reading responses

Once configured, your AI Assistant is **fully functional and completely free!** 🎉
