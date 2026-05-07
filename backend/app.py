from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    question = data.get("question", "").lower()

    if "ai" in question:
        answer = "AI stands for Artificial Intelligence. It helps machines think like humans."

    elif "python" in question:
        answer = "Python is a programming language."

    elif "html" in question:
        answer = "HTML is used to create web pages."

    else:
        answer = "I understood your question: " + question

    return jsonify({
        "answer": answer
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)