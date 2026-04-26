import os
from ollama import Client
from dotenv import load_dotenv

load_dotenv()

client = Client(
  host="https://ollama.com",
  headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY')}
)

print("--- Ollama running ---")
print("Type 'exit' or 'quit' to stop.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ['exit', 'quit']:
        break

    messages = [
      {
        'role': 'user',
        'content': user_input,
      },
    ]
    
    print("AI: ", end='', flush=True)
    
    try:
        for part in client.chat('gpt-oss:120b-cloud', messages=messages, stream=True):
          print(part['message']['content'], end='', flush=True)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        
    print("\n")