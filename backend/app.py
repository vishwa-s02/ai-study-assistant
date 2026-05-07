from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # 🔥 This fixes your error

@app.route("/")
def home():
    return "AI Study Assistant Running 🚀"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "").lower()

    # Fake AI logic
    if "ai" in question:
        answer = "AI (Artificial Intelligence) is the simulation of human intelligence by machines."
    elif "os" in question or "operating system" in question:
        answer = "An Operating System manages hardware and software resources."
    elif "dbms" in question:
        answer = "DBMS is a system to store, manage, and retrieve data."
    else:
        answer = "This is a demo AI response. You can connect a real AI API later."

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)