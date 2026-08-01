import os
import requests
import pandas as pd
from edgar import Company, set_identity
from datetime import date, timedelta

set_identity("williamsabate2006@gmail.com")

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def enviar_telegram(mensaje):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": mensaje}
    )

ARCHIVO_HISTORIAL = "ya_avisados.txt"
if os.path.exists(ARCHIVO_HISTORIAL):
    with open(ARCHIVO_HISTORIAL, "r") as f:
        ya_avisados = set(line.strip() for line in f)
else:
    ya_avisados = set()

tickers = ["TSLA", "NVDA", "AMD", "PLTR", "COIN", "SNOW", "RIVN", "SOFI", "UPST", "AFRM"]
desde = (date.today() - timedelta(days=30)).isoformat()
hasta = date.today().isoformat()

todas = []
for ticker in tickers:
    empresa = Company(ticker)
    filings = empresa.get_filings(form=4, filing_date=f"{desde}:{hasta}")
    for f in filings:
        todas.append(f.obj().to_dataframe().fillna(''))

transacciones = pd.concat(todas)
compras_reales = transacciones[transacciones['Code'] == 'P'].copy()
compras_reales['Date'] = pd.to_datetime(compras_reales['Date'])

nuevas = 0
for _, row in compras_reales.iterrows():
    clave = f"{row['Ticker']}_{row['Insider']}_{row['Date']}_{row['Shares']}"
    if clave in ya_avisados:
        continue

    mensaje = (
        f"🟢 Compra de insider\n"
        f"{row['Insider']} ({row['Position']})\n"
        f"{row['Issuer']} ({row['Ticker']})\n"
        f"{row['Shares']:,.0f} acciones por ${row['Value']:,.0f}\n"
        f"Fecha: {row['Date'].strftime('%Y-%m-%d')}"
    )
    enviar_telegram(mensaje)
    ya_avisados.add(clave)
    nuevas += 1

with open(ARCHIVO_HISTORIAL, "w") as f:
    for clave in sorted(ya_avisados):
        f.write(clave + "\n")

print(f"Nuevas notificadas: {nuevas}")
print(f"Total en historial: {len(ya_avisados)}")
