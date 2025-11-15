# AI Chatbot - Frontend & Backend Setup

A modern web-based chatbot interface powered by OpenAI's GPT API.

## 📁 Files Overview

- **`index.html`** - Frontend chatbot interface
- **`style.css`** - Styling for the chatbot UI
- **`script.js`** - Frontend JavaScript logic
- **`app.py`** - Flask backend server
- **`chatbotManager.py`** - OpenAI API integration

## 🚀 Quick Start

### 1. Set Your OpenAI API Key

**Windows PowerShell:**
```powershell
$env:OPENAI_API_KEY = "your-openai-api-key-here"
```

**Windows CMD:**
```cmd
set OPENAI_API_KEY=your-openai-api-key-here
```

### 2. Install Dependencies

All packages should already be installed, but if needed:
```bash
pip install openai flask flask-cors
```

### 3. Start the Backend Server

```bash
python app.py
```

You should see:
```
🚀 Starting Flask server...
Frontend: Open index.html in your browser
API Server: http://localhost:5000
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
```

### 4. Open the Frontend

Open `index.html` in your web browser (double-click the file or drag it into your browser)

## 🎨 Features

- **Clean, Modern UI** - Beautiful gradient design with smooth animations
- **Real-time Chat** - Send and receive messages instantly
- **Configurable Settings**:
  - Choose between GPT-3.5 Turbo, GPT-4, or GPT-4 Turbo
  - Adjust temperature for creativity (0-2)
  - Set max tokens for response length
- **Conversation History** - The backend maintains context across messages
- **Responsive Design** - Works on desktop and mobile devices
- **Loading Animation** - Visual feedback while waiting for responses
- **Clear Chat** - Start fresh with the clear button

## 📋 How to Use

1. Type your message in the input field
2. Press Enter or click the send button (➤)
3. Wait for the AI response
4. Adjust settings on the right sidebar if needed
5. Click "Clear Chat" to start a new conversation

## 🔧 Settings Explained

### Model
- **GPT-3.5 Turbo**: Fast, cost-effective (default)
- **GPT-4**: More powerful and accurate
- **GPT-4 Turbo**: Faster GPT-4 with larger context window

### Temperature (0.0 - 2.0)
- **0.0-0.3**: Deterministic, factual responses
- **0.5-0.8**: Balanced (recommended, default: 0.7)
- **1.5-2.0**: Creative, random responses

### Max Tokens
- Controls the maximum length of responses
- Higher values = longer responses
- Range: 50-2000 (default: 150)

## 🔌 API Endpoints

### POST `/api/chat`
Send a single message with customizable parameters
```json
{
  "message": "Hello!",
  "model": "gpt-3.5-turbo",
  "temperature": 0.7,
  "max_tokens": 150
}
```

### POST `/api/chat-with-context`
Send a message using full conversation history for better context
```json
{
  "message": "Tell me more",
  "model": "gpt-3.5-turbo"
}
```

### POST `/api/clear`
Clear the conversation history

### GET `/api/health`
Check if the server is running and API key is configured

## 🐛 Troubleshooting

### "Connection refused" or "Cannot reach server"
- Make sure the Flask server is running (`python app.py`)
- Check that it's running on `http://localhost:5000`
- Try accessing `http://localhost:5000` in your browser to verify

### "API Key not set" warning
- Set your OpenAI API key as shown in the Quick Start section
- The key must be set BEFORE starting the Flask server
- Get your key from: https://platform.openai.com/api-keys

### "Failed to get response" error
- Check your API key is valid
- Verify you have sufficient API credits
- Check the console (F12) for detailed error messages
- Make sure your OpenAI account has access to the model you selected

### Empty response or timeout
- The AI might be taking longer than expected
- Try a simpler prompt
- Check your internet connection
- Consider lowering max_tokens

## 📚 Customization

### Change Default Model
Edit in `script.js`:
```javascript
model: 'gpt-4' // Change this line
```

### Change Server Port
Edit in `app.py`:
```python
app.run(debug=True, port=8000) # Change port from 5000 to 8000
```

Also update `API_BASE_URL` in `script.js`:
```javascript
const API_BASE_URL = 'http://localhost:8000/api';
```

### Change UI Colors
Edit the gradient in `style.css`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
/* Change these hex colors to your preference */
```

## 📝 Code Structure

### chatbotManager.py
- `generate_text()` - Simple text generation
- `chat_with_context()` - Conversation with full context

### app.py
- Flask server with CORS support
- Stores conversation history
- Manages API communication

### Frontend (HTML/CSS/JS)
- Real-time message display
- Settings panel for customization
- Error handling and user feedback

## 🔐 Security Notes

- Never commit your `.env` or API keys to git
- Store API keys in environment variables only
- The frontend never directly handles API keys
- All communication goes through your local backend server

## 📦 Dependencies

- `openai` - Official OpenAI Python library
- `flask` - Web framework
- `flask-cors` - Enable cross-origin requests

## 🎯 Next Steps

- Customize the UI colors and fonts
- Add user authentication
- Store chat history in a database
- Deploy to a web server
- Add support for file uploads
- Implement multi-user support

Enjoy your AI Chatbot! 🤖
