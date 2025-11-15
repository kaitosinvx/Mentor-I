// Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// DOM Elements
const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const clearBtn = document.getElementById('clearBtn');
const modelSelect = document.getElementById('modelSelect');
const temperatureSlider = document.getElementById('temperatureSlider');
const maxTokens = document.getElementById('maxTokens');
const tempValue = document.getElementById('tempValue');
const tokenValue = document.getElementById('tokenValue');

// Settings object
let settings = {
    model: 'gpt-3.5-turbo',
    temperature: 0.7,
    maxTokens: 150
};

// Event listeners
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

clearBtn.addEventListener('click', clearChat);

modelSelect.addEventListener('change', (e) => {
    settings.model = e.target.value;
});

temperatureSlider.addEventListener('input', (e) => {
    settings.temperature = parseFloat(e.target.value);
    tempValue.textContent = settings.temperature.toFixed(1);
});

maxTokens.addEventListener('input', (e) => {
    settings.maxTokens = parseInt(e.target.value);
    tokenValue.textContent = settings.maxTokens;
});

// Main functions
async function sendMessage() {
    const message = userInput.value.trim();
    
    if (!message) return;

    // Add user message to chat
    addMessage('user', message);
    userInput.value = '';
    userInput.focus();

    // Disable send button and show loading
    sendBtn.disabled = true;
    
    // Add loading indicator
    const loadingId = addLoadingMessage();

    try {
        // Send to backend
        const response = await fetch(`${API_BASE_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                model: settings.model,
                temperature: settings.temperature,
                max_tokens: settings.maxTokens
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        // Remove loading message
        removeLoadingMessage(loadingId);
        
        // Add assistant response
        addMessage('assistant', data.response);

    } catch (error) {
        console.error('Error:', error);
        removeLoadingMessage(loadingId);
        addMessage('assistant', `Sorry, I encountered an error: ${error.message}. Make sure the backend server is running on http://localhost:5000`);
    } finally {
        sendBtn.disabled = false;
    }
}

function addMessage(role, content) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${role}-message`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.textContent = content;
    
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    return messageDiv;
}

function addLoadingMessage() {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message assistant-message';
    messageDiv.id = `loading-${Date.now()}`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content loading';
    contentDiv.innerHTML = '<span></span><span></span><span></span>';
    
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    return messageDiv.id;
}

function removeLoadingMessage(id) {
    const loadingMessage = document.getElementById(id);
    if (loadingMessage) {
        loadingMessage.remove();
    }
}

function clearChat() {
    if (confirm('Are you sure you want to clear the chat history?')) {
        chatMessages.innerHTML = '';
        addMessage('assistant', 'Chat cleared! How can I help you today?');
    }
}

// Initialize
console.log('ChatBot UI loaded successfully');
console.log('Make sure to run the Flask backend server on http://localhost:5000');
