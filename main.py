import os
import requests

TOKEN = os.environ["8994820850:AAEMSgs4lwT0PEAf9VV8WgaLxZehcBTp9-4"]
CHAT_ID = os.environ["6420362893"]

respuesta = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": "✅ Prueba 2 desde GitHub Actions"}
)

print("Código:", respuesta.status_code)
print("Respuesta:", respuesta.text)
