 # BitcoinPay - TPV Lightning para emprendedores

Proyecto que permite a negocios aceptar Bitcoin Lightning usando LNbits.

## Funcionalidades
- Generación de invoices
- Código QR dinámico
- Pagos con Zeus Lightning Wallet
- Verificación del estado del pago
- División de pagos (Split Payments LNbits)

## Tecnologías
- Python (Flask)
- HTML, CSS, JS
- LNbits API
- Zeus Wallet

## Cómo ejecutar

### Backend
cd backend  
pip install -r requirements.txt  
python app.py

### Frontend
Abrir frontend/index.html

Proyecto con integración de pagos Lightning con LNBits.

## Instalación

1. Instalar dependencias:
   pip install -r requirements.txt

2. Crear archivo .env basado en .env.example

## Ejecutar el backend
uvicorn app:app --reload
