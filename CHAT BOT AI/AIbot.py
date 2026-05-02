import requests

def chat_with_ai(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"You are a veterinary doctor. Answer clearly.\nUser: {prompt}",
            "stream": False
        }
    )
    
    return response.json()["response"]


while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit"]:
        break
    
    reply = chat_with_ai(user_input)
    print("Bot:", reply)