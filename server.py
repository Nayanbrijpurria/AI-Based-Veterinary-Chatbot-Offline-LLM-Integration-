

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():

    user_message = request.json.get("message")

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            #"model": "llama3",-----------------> I CHANGE THIS MODEL BECAUSE THE 7B MODEL IS TOO HEAVY FOR MY GPU, I USE THE 3B MODEL INSTEAD
            "model": "llama3.2:3b",  
            "prompt": f"You are a veterinary doctor. Answer clearly in easy language. Also prescribe medication if necessary.\nUser: {user_message}",
            "stream": True,
            "options": {
              "num_predict": 150
            }
        }
    )

    answer = response.json()["response"]

    return jsonify({
        "response": answer
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
