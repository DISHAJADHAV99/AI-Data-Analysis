
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/dashboard", methods=["GET"])
def dashboard():

    data = {
        "total_sales": 322966.75,
        "average_sale": 322.97,
        "highest_sale": 1042.65,
        "total_quantity": 5510,
        "transactions": 1000
    }

    return jsonify(data)

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data.get("question")

    if not question:
        return jsonify({"error": "Question is required"}), 400

    return jsonify({
        "question": question,
        "answer": "AI Data Analyst API is working."
    })

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
