import requests
import os

LNBITS_URL = os.getenv("LNBITS_URL")
LNBITS_API_KEY = os.getenv("LNBITS_API_KEY")


def crear_invoice_lnbits(amount, memo):
    url = f"{LNBITS_URL}/api/v1/payments"

    headers = {
        "X-Api-Key": LNBITS_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "out": False,
        "amount": int(amount),
        "memo": memo
    }

    try:
        r = requests.post(url, json=data, headers=headers, timeout=10)

        # Si LNbits devuelve error (400, 403, 500…) lo atrapamos aquí
        r.raise_for_status()

        return r.json()

    except requests.exceptions.RequestException as e:
        print("⚠️ ERROR conectando con LNbits:", e)

        # Regresamos una respuesta controlada
        return {
            "error": True,
            "message": "No se pudo crear el invoice en LNbits.",
            "details": str(e)
        }


def consultar_pago_lnbits(payment_id):
    url = f"{LNBITS_URL}/api/v1/payments/{payment_id}"

    headers = {
        "X-Api-Key": LNBITS_API_KEY
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        return r.json()

    except requests.exceptions.RequestException as e:
        print("⚠️ ERROR verificando pago en LNbits:", e)
        return {
            "error": True,
            "message": "No se pudo verificar el pago.",
            "details": str(e)
        }

