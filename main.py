import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

respuesta = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": "✅ Prueba 2 desde GitHub Actions"}
)

print("Código:", respuesta.status_code)
print("Respuesta:", respuesta.text)
