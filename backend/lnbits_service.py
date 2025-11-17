import requests
import os

LNBITS_URL = "http://chirilicas.com:5000"
LNBITS_API_KEY = "8c02d6233c204dadb4b977e1a733130d"



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

    r = requests.post(url, json=data, headers=headers)
    r.raise_for_status()
    return r.json()


def consultar_pago_lnbits(payment_id):
    url = f"{LNBITS_URL}/api/v1/payments/{payment_id}"

    headers = {
        "X-Api-Key": LNBITS_API_KEY
    }

    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()
