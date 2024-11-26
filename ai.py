from anthropic import Anthropic
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Anthropic client with your API key
anthropic = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def chat_with_claude(message):
    try:
        response = anthropic.messages.create(
            model="claude-3-sonnet-20240229",  # You can also use "claude-3-opus-20240229" for better results
            max_tokens=1000,
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Claude: Hello! I'm your AI assistant. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("Claude: Goodbye!")
            break
            
        response = chat_with_claude(user_input)
        print("Claude:", response)

if __name__ == "__main__":
    main()

def chat_with_claude(message, conversation_history):
    try:
        messages = conversation_history + [{"role": "user", "content": message}]
        response = anthropic.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=messages
        )
        conversation_history.append({"role": "user", "content": message})
        conversation_history.append({"role": "assistant", "content": response.content[0].text})
        return response.content[0].text, conversation_history
    except Exception as e:
        return f"An error occurred: {str(e)}", conversation_history

def main():
    print("Claude: Hello! I'm your AI assistant. Type 'quit' to exit.")
    conversation_history = []
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("Claude: Goodbye!")
            break
            
        response, conversation_history = chat_with_claude(user_input, conversation_history)
        print("Claude:", response)