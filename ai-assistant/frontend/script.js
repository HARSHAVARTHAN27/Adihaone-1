// Modern AI Assistant - Script
// Configuration
const API_BASE_URL = 'http://localhost:5000/api';
let isListening = false;
let autoSpeakEnabled = true;
let recognition = null;
let isDarkMode = localStorage.getItem('darkMode') === 'true';

// Initialize Speech Recognition
if ('webkitSpeechRecognition' in window) {
    recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';

    recognition.onstart = () => {
        isListening = true;
        document.getElementById('voiceBtn').classList.add('recording');
        document.getElementById('voiceStatus').textContent = '🎤 Listening...';
    };

    recognition.onend = () => {
        isListening = false;
        document.getElementById('voiceBtn').classList.remove('recording');
        document.getElementById('voiceStatus').textContent = '';
    };

    recognition.onerror = (event) => {
        console.error('Speech recognition error:', event.error);
        document.getElementById('voiceStatus').textContent = `❌ Error: ${event.error}`;
    };

    recognition.onresult = (event) => {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; i++) {
            transcript += event.results[i][0].transcript;
        }
        document.getElementById('textInput').value = transcript;
        sendMessage();
    };
}

// DOM Elements
const chatMessages = document.getElementById('chatMessages');
const textInput = document.getElementById('textInput');
const sendBtn = document.getElementById('sendBtn');
const voiceBtn = document.getElementById('voiceBtn');
const darkModeToggle = document.getElementById('darkModeToggle');
const settingsBtn = document.getElementById('settingsBtn');
const settingsModal = document.getElementById('settingsModal');
const closeSettingsBtn = document.getElementById('closeSettingsBtn');
const closeSettingsBtn2 = document.getElementById('closeSettingsBtn2');
const modelSelect = document.getElementById('modelSelect');
const voiceSelect = document.getElementById('voiceSelect');
const autoSpeakCheckbox = document.getElementById('autoSpeakCheckbox');
const voiceToggle = document.getElementById('voiceToggle');
const rateSlider = document.getElementById('rateSlider');
const volumeSlider = document.getElementById('volumeSlider');
const rateValue = document.getElementById('rateValue');
const volumeValue = document.getElementById('volumeValue');
const clearHistoryBtn = document.getElementById('clearHistoryBtn');
const historyList = document.getElementById('historyList');
const statusInfo = document.getElementById('statusInfo');
const toast = document.getElementById('toast');

// Event Listeners
sendBtn.addEventListener('click', sendMessage);
textInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

voiceBtn.addEventListener('click', startVoiceInput);
darkModeToggle.addEventListener('click', toggleDarkMode);
settingsBtn.addEventListener('click', openSettings);
closeSettingsBtn.addEventListener('click', closeSettings);
closeSettingsBtn2.addEventListener('click', closeSettings);
voiceToggle.addEventListener('click', toggleAutoSpeak);
voiceSelect.addEventListener('change', updateVoice);
rateSlider.addEventListener('input', updateRate);
volumeSlider.addEventListener('input', updateVolume);
clearHistoryBtn.addEventListener('click', clearHistory);
autoSpeakCheckbox.addEventListener('change', toggleAutoSpeakCheckbox);

// Quick actions
document.querySelectorAll('.quick-action').forEach(btn => {
    btn.addEventListener('click', () => {
        textInput.value = btn.getAttribute('data-prompt');
        sendMessage();
    });
});

// Initialize
window.addEventListener('load', initialize);

async function initialize() {
    // Load dark mode
    if (isDarkMode) {
        document.body.classList.add('dark-mode');
    }

    // Load settings
    loadSettings();

    // Check connection
    checkConnection();

    // Load models
    loadModels();

    // Load voices
    loadVoices();

    // Load history
    loadHistory();

    // Auto-check connection every 30 seconds
    setInterval(checkConnection, 30000);
}

async function sendMessage() {
    const text = textInput.value.trim();

    if (!text) {
        showToast('Please enter a message', 'warning');
        return;
    }

    // Add user message to chat
    addMessage(text, 'user');
    textInput.value = '';

    // Disable input while processing
    sendBtn.disabled = true;
    textInput.disabled = true;

    try {
        // Add loading indicator
        const loadingId = addMessage('Thinking...', 'assistant', true);

        const response = await fetch(`${API_BASE_URL}/process_text`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Remove loading indicator
        const loadingElement = document.querySelector(`[data-id="${loadingId}"]`);
        if (loadingElement) {
            loadingElement.remove();
        }

        // Add assistant response
        addMessage(data.response || 'No response received', 'assistant');

        // Update history
        loadHistory();

        // Show success
        if (!data.error) {
            showToast('✓ Response received', 'success');
        }

    } catch (error) {
        console.error('Error:', error);
        addMessage(`Error: ${error.message}`, 'assistant');
        showToast('Error sending message', 'error');
    } finally {
        sendBtn.disabled = false;
        textInput.disabled = false;
        textInput.focus();
    }
}

function addMessage(text, role, isLoading = false) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', `${role}-message`);

    const bubble = document.createElement('div');
    bubble.classList.add('message-bubble');

    // Create unique ID for loading messages
    const msgId = `msg-${Date.now()}-${Math.random()}`;
    messageDiv.setAttribute('data-id', msgId);

    if (isLoading) {
        bubble.innerHTML = `<p><em>${text}</em></p>`;
    } else {
        // Parse and format the response
        const formattedText = text
            .replace(/\n\n/g, '</p><p>')
            .replace(/\n/g, '<br>')
            .split('</p><p>')
            .map(p => `<p>${p}</p>`)
            .join('');

        bubble.innerHTML = formattedText;
    }

    messageDiv.appendChild(bubble);
    chatMessages.appendChild(messageDiv);

    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;

    return msgId;
}

function startVoiceInput() {
    if (!recognition) {
        showToast('Voice recognition not supported', 'error');
        return;
    }

    if (isListening) {
        recognition.abort();
    } else {
        recognition.start();
    }
}

function updateRate() {
    const rate = rateSlider.value;
    rateValue.textContent = rate;
    fetch(`${API_BASE_URL}/tts/settings`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rate: parseInt(rate) })
    });
}

function updateVolume() {
    const volume = volumeSlider.value;
    volumeValue.textContent = volume;
    fetch(`${API_BASE_URL}/tts/settings`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ volume: parseInt(volume) / 100 })
    });
}

function toggleDarkMode() {
    isDarkMode = !isDarkMode;
    document.body.classList.toggle('dark-mode', isDarkMode);
    localStorage.setItem('darkMode', isDarkMode);
    darkModeToggle.classList.toggle('active', isDarkMode);
    showToast(isDarkMode ? '🌙 Dark mode' : '☀️ Light mode');
}

function toggleAutoSpeak() {
    autoSpeakEnabled = !autoSpeakEnabled;
    voiceToggle.classList.toggle('active', autoSpeakEnabled);
    fetch(`${API_BASE_URL}/speak_toggle`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ enabled: autoSpeakEnabled })
    });
    showToast(`Auto-speak ${autoSpeakEnabled ? 'enabled' : 'disabled'}`);
}

function toggleAutoSpeakCheckbox() {
    autoSpeakEnabled = autoSpeakCheckbox.checked;
    fetch(`${API_BASE_URL}/speak_toggle`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ enabled: autoSpeakEnabled })
    });
}

function openSettings() {
    settingsModal.classList.add('show');
}

function closeSettings() {
    settingsModal.classList.remove('show');
}

async function loadModels() {
    try {
        const response = await fetch(`${API_BASE_URL}/models`);
        const data = await response.json();

        modelSelect.innerHTML = '';
        if (data.models && data.models.length > 0) {
            data.models.forEach(model => {
                const option = document.createElement('option');
                option.value = model;
                option.textContent = model;
                if (model === data.current_model) {
                    option.selected = true;
                }
                modelSelect.appendChild(option);
            });
        } else {
            const option = document.createElement('option');
            option.textContent = 'No models available';
            modelSelect.appendChild(option);
        }

        modelSelect.addEventListener('change', async () => {
            const selected = modelSelect.value;
            const resp = await fetch(`${API_BASE_URL}/model/set`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ model: selected })
            });
            const result = await resp.json();
            showToast(result.message, 'success');
        });
    } catch (error) {
        console.error('Error loading models:', error);
        modelSelect.innerHTML = '<option>Error loading models</option>';
    }
}

async function loadHistory() {
    try {
        const response = await fetch(`${API_BASE_URL}/history?limit=10`);
        const data = await response.json();

        historyList.innerHTML = '';
        if (data.history && data.history.length > 0) {
            data.history.forEach(item => {
                const historyItem = document.createElement('div');
                historyItem.classList.add('history-item');
                historyItem.textContent = item.user.substring(0, 30) + (item.user.length > 30 ? '...' : '');
                historyItem.title = item.user;
                historyItem.addEventListener('click', () => {
                    textInput.value = item.user;
                    sendMessage();
                });
                historyList.appendChild(historyItem);
            });
        } else {
            const emptyMsg = document.createElement('div');
            emptyMsg.textContent = 'No history';
            emptyMsg.style.opacity = '0.5';
            historyList.appendChild(emptyMsg);
        }
    } catch (error) {
        console.error('Error loading history:', error);
    }
}

async function clearHistory() {
    if (confirm('Clear all conversation history?')) {
        try {
            await fetch(`${API_BASE_URL}/clear_history`, { method: 'POST' });
            chatMessages.innerHTML = '';
            addMessage('Conversation cleared. How can I help you?', 'system');
            loadHistory();
            showToast('History cleared', 'success');
        } catch (error) {
            showToast('Error clearing history', 'error');
        }
    }
}

async function checkConnection() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        const data = await response.json();

        statusInfo.classList.remove('error');
        statusInfo.classList.add('connected');
        statusInfo.innerHTML = `
            <span class="status-dot"></span>
            <strong>Connected</strong><br>
            <small>Model: ${data.model || 'unknown'}<br>
            Auto-speak: ${data.auto_speak ? '✓' : '✗'}</small>
        `;
    } catch (error) {
        statusInfo.classList.remove('connected');
        statusInfo.classList.add('error');
        statusInfo.innerHTML = `
            <strong>⚠️ Disconnected</strong><br>
            <small>Cannot reach backend</small>
        `;
    }
}

function showToast(message, type = 'info') {
    toast.textContent = message;
    toast.className = `toast show ${type}`;

    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

function loadSettings() {
    autoSpeakCheckbox.checked = autoSpeakEnabled;
    voiceToggle.classList.toggle('active', autoSpeakEnabled);
    rateSlider.value = localStorage.getItem('rate') || 150;
    volumeSlider.value = localStorage.getItem('volume') || 100;
    rateValue.textContent = rateSlider.value;
    volumeValue.textContent = volumeSlider.value;
}

async function loadVoices() {
    try {
        const response = await fetch(`${API_BASE_URL}/tts/voices`);
        const data = await response.json();

        voiceSelect.innerHTML = '';
        if (data.voices && data.voices.length > 0) {
            data.voices.forEach((voice, index) => {
                const option = document.createElement('option');
                option.value = index;
                option.textContent = voice.name || `Voice ${index + 1}`;
                voiceSelect.appendChild(option);
            });
            
            // Load saved voice preference
            const savedVoice = localStorage.getItem('selectedVoice') || '0';
            voiceSelect.value = savedVoice;
        } else {
            const option = document.createElement('option');
            option.textContent = 'No voices available';
            voiceSelect.appendChild(option);
        }
    } catch (error) {
        console.error('Error loading voices:', error);
        voiceSelect.innerHTML = '<option>Error loading voices</option>';
    }
}

async function updateVoice() {
    const voiceIndex = parseInt(voiceSelect.value);
    try {
        const response = await fetch(`${API_BASE_URL}/tts/settings`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ voice_index: voiceIndex })
        });
        const result = await response.json();
        localStorage.setItem('selectedVoice', voiceIndex);
        showToast('Voice changed', 'success');
    } catch (error) {
        console.error('Error updating voice:', error);
        showToast('Failed to change voice', 'error');
    }
}

window.addEventListener('beforeunload', () => {
    localStorage.setItem('rate', rateSlider.value);
    localStorage.setItem('volume', volumeSlider.value);
});
