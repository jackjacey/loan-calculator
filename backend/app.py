import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    principal = float(data["principal"])
    annual_rate = float(data["annual_rate"]) / 100
    months = int(data["months"])

    if annual_rate == 0:
        monthly_payment = principal / months
    else:
        monthly_rate = annual_rate / 12
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / \
                          ((1 + monthly_rate) ** months - 1)

    total_payment = monthly_payment * months
    total_interest = total_payment - principal

    return jsonify({
        "monthly_payment": round(monthly_payment, 2),
        "total_payment": round(total_payment, 2),
        "total_interest": round(total_interest, 2)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)