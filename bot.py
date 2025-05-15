
import os
import time
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("GROUP_ID", "-100")  # Telegram group ID
POSTED_FILE = "posted.txt"
INFO_FILE = "info.txt"

def read_info():
    with open(INFO_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def read_posted():
    if not os.path.exists(POSTED_FILE):
        return set()
    with open(POSTED_FILE, "r") as f:
        return set(line.strip() for line in f)

def mark_posted(msg):
    with open(POSTED_FILE, "a") as f:
        f.write(msg + "\n")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    requests.post(url, data=data)

if __name__ == "__main__":
    while True:
        posted = read_posted()
        lines = read_info()
        for line in lines:
            if line not in posted:
                send_message(line)
                mark_posted(line)
        time.sleep(60)  # check every 1 minute
