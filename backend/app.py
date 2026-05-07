from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS
CORS(app)

# Home route
@app.route("/")
def home():
    return "AI Study Assistant Backend is Running!"

# Ask route
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    question = data.get("question", "").lower()

    # Simple AI responses
    answers = {
        "what is ai": "AI stands for Artificial Intelligence.",
        "what is python": "Python is a programming language.",
        "what is html": "HTML is used to create web pages.",
        "what is css": "CSS is used for styling web pages.",
        "what is javascript": "JavaScript makes websites interactive."
    }

    answer = answers.get(
        question,
        "Sorry, I don't know the answer yet."
    )

    return jsonify({
        "answer": answer
    })

# Run Flask app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )