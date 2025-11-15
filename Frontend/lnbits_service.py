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

    r = requests.post(url, json=data, headers=headers)
    r.raise_for_status()
    return r.json()

