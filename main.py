import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

print("Largo del TOKEN:", len(TOKEN))
print("Contiene ':':", ":" in TOKEN)
print("Primeros 3 caracteres:", repr(TOKEN[:3]))
print("Últimos 3 caracteres:", repr(TOKEN[-3:]))
print("Largo del CHAT_ID:", len(CHAT_ID))

respuesta = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": "✅ Prueba 4"}
)
print("Código:", respuesta.status_code)
print("Respuesta:", respuesta.text)
