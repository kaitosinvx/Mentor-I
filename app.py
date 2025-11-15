from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbotManager import generate_text, chat_with_context
import os

app = Flask(__name__)
CORS(app)

# Store conversation history for context
conversation_history = []


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    API endpoint for chat requests
    Expects JSON with: message, model, temperature, max_tokens
    """
    try:
        data = request.json
        user_message = data.get('message')
        model = data.get('model', 'gpt-3.5-turbo')
        temperature = data.get('temperature', 0.7)
        max_tokens = data.get('max_tokens', 150)

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Add user message to history
        conversation_history.append({
            'role': 'user',
            'content': user_message
        })

        # Get response from OpenAI
        response = generate_text(
            prompt=user_message,
            model=model,
            max_tokens=max_tokens
        )

        if not response:
            return jsonify({'error': 'Failed to get response from API'}), 500

        # Add assistant response to history
        conversation_history.append({
            'role': 'assistant',
            'content': response
        })

        return jsonify({
            'response': response,
            'model': model,
            'message_count': len(conversation_history)
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/chat-with-context', methods=['POST'])
def chat_endpoint():
    """
    Alternative endpoint that uses full conversation context
    """
    try:
        data = request.json
        user_message = data.get('message')
        model = data.get('model', 'gpt-3.5-turbo')

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Add user message to history
        conversation_history.append({
            'role': 'user',
            'content': user_message
        })

        # Get response with full context
        response = chat_with_context(
            messages=conversation_history,
            model=model
        )

        if not response:
            return jsonify({'error': 'Failed to get response from API'}), 500

        # Add assistant response to history
        conversation_history.append({
            'role': 'assistant',
            'content': response
        })

        return jsonify({
            'response': response,
            'model': model,
            'message_count': len(conversation_history)
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/clear', methods=['POST'])
def clear_history():
    """
    Clear conversation history
    """
    global conversation_history
    conversation_history = []
    return jsonify({'message': 'Conversation history cleared'})


@app.route('/api/health', methods=['GET'])
def health():
    """
    Health check endpoint
    """
    return jsonify({
        'status': 'healthy',
        'api_key_configured': bool(os.getenv('OPENAI_API_KEY'))
    })


@app.route('/', methods=['GET'])
def index():
    """
    Serve the frontend
    """
    return '''
    <h1>API Server Running</h1>
    <p>Visit the frontend HTML file to use the chatbot</p>
    <ul>
        <li>POST /api/chat - Send a message</li>
        <li>POST /api/chat-with-context - Send a message with full conversation context</li>
        <li>POST /api/clear - Clear conversation history</li>
        <li>GET /api/health - Check server health</li>
    </ul>
    '''


if __name__ == '__main__':
    # Check if API key is set
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  WARNING: OPENAI_API_KEY environment variable is not set!")
        print("Please set your API key before running this server:")
        print("  Windows (PowerShell): $env:OPENAI_API_KEY = 'your-key-here'")
        print("  Windows (CMD): set OPENAI_API_KEY=your-key-here")
        print("  Linux/Mac: export OPENAI_API_KEY=your-key-here")
    
    print("🚀 Starting Flask server...")
    print("Frontend: Open index.html in your browser")
    print("API Server: http://localhost:5000")
    app.run(debug=True, port=5000)
