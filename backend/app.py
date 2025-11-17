from flask import Flask, jsonify, request
from flask_cors import CORS
from crear_invoice import crear_invoice, consultar_pago_lnbits
from dotenv import load_dotenv
import os

# Cargar credenciales desde .env
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

app = Flask(__name__)
CORS(app)

# HABILITAR CORS PARA QUE EL FRONTEND PUEDA HACER PETICIONES
CORS(app)

# Crear un invoice
@app.route("/api/invoice", methods=["POST"])
def api_invoice():
    data = request.get_json() or {}
    amount = int(data.get("amount", 100))  # sats
    memo = data.get("memo", "Pago desde BitcoinPay")

    result = crear_invoice(amount, memo)
    return jsonify(result)

# Consultar el estado de un pago
@app.route("/api/status/<payment_id>", methods=["GET"])
def api_status(payment_id):
    estado = verificar_pago(payment_id)
    return jsonify(estado)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")