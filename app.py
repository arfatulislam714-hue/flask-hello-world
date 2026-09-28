import os
import random
import time
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = "8909293442:AAFH36v1p4CbsvKo3fEi0Ev7a3k-tceF0Go"

def send_signal(chat_id):
    prediction = random.choice(["BIG 🟢", "SMALL 🔴"])
    period = int(time.time()) // 30
    text = (
        f"🤖 **My Helper Bot**\n"
        f"👤 **Developer:** Arfat ul Islam\n\n"
        f"🎯 **Signal Prediction**\n"
        f"📌 **Period:** #{period}\n"
        f"🎲 **Result:** {prediction}\n"
        f"⚡ **Strategy:** Martingale Step 1\n\n"
        f"⏱️ Next Signal in 30s!"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text, "parse_mode": "Markdown"})

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        data = request.get_json()
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")
            if text == "/start":
                send_signal(chat_id)
        return "OK", 200
    return "Bot Server is Running!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
