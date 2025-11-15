from lnbits_service import crear_invoice_lnbits, consultar_pago_lnbits
import qrcode
import base64
import io

def crear_invoice(amount, memo):
    # Crear invoice en LNbits
    respuesta = crear_invoice_lnbits(amount, memo)

    payment_request = respuesta["payment_request"]
    payment_id = respuesta["payment_hash"]

    # Generar QR en base64
    img = qrcode.make(payment_request)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    qr_b64 = base64.b64encode(buffer.getvalue()).decode()

    return {
        "payment_request": payment_request,
        "payment_id": payment_id,
        "qr_base64": qr_b64
    }

def verificar_pago(payment_id):
    return consultar_pago_lnbits(payment_id)
