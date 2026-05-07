from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI Study Assistant Backend Running"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").lower()

    if "ai" in question:
        answer = "AI stands for Artificial Intelligence. It enables machines to think and learn like humans."

    elif "python" in question:
        answer = "Python is a popular programming language used for web development, AI, and automation."

    elif "html" in question:
        answer = "HTML is used to create webpages."

    elif "css" in question:
        answer = "CSS is used to style webpages."

    elif "javascript" in question:
        answer = "JavaScript adds interactivity to websites."

    else:
        answer = "Sorry, I don't know the answer yet."

    return jsonify({
        "answer": answer
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)