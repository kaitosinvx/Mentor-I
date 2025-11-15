import os
import openai
from openai import OpenAI

# Initialize the OpenAI client
# Make sure to set your API key as an environment variable: OPENAI_API_KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_text(prompt: str, model: str = "gpt-3.5-turbo", max_tokens: int = 150) -> str:
    """
    Generate text using OpenAI's API.
    
    Args:
        prompt (str): The input prompt for text generation
        model (str): The model to use (default: gpt-3.5-turbo)
        max_tokens (int): Maximum tokens in the response (default: 150)
    
    Returns:
        str: The generated text response
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].message.content
    except openai.APIError as e:
        print(f"OpenAI API error: {e}")
        return ""


def chat_with_context(messages: list, model: str = "gpt-3.5-turbo") -> str:
    """
    Have a conversation with context using OpenAI's API.
    
    Args:
        messages (list): List of message dictionaries with 'role' and 'content'
        model (str): The model to use (default: gpt-3.5-turbo)
    
    Returns:
        str: The generated response
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
    except openai.APIError as e:
        print(f"OpenAI API error: {e}")
        return ""


if __name__ == "__main__":
    # Example usage
    prompt = "What is the capital of France?"
    response = generate_text(prompt)
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")
