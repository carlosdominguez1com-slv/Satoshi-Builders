from lnbits_service import crear_invoice_lnbits, consultar_pago_lnbits
import qrcode
import base64
import io

def crear_invoice(amount, memo):
    respuesta = crear_invoice_lnbits(amount, memo)

    # Manejo de error
    if "error" in respuesta:
        return respuesta

    payment_request = respuesta["payment_request"]
    payment_id = respuesta["payment_hash"]

    # Crear QR
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
