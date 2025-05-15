import os
import time
import requests

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

INFO_FILE = "info.txt"
POSTED_FILE = "posted.txt"

def read_info():
    if not os.path.exists(INFO_FILE):
        return []
    with open(INFO_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def read_posted():
    if not os.path.exists(POSTED_FILE):
        return set()
    with open(POSTED_FILE, "r") as f:
        return set(line.strip() for line in f if line.strip())

def write_posted(posted):
    with open(POSTED_FILE, "w") as f:
        for item in posted:
            f.write(f"{item}\n")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

def run_bot():
    posted = read_posted()
    info = read_info()
    for line in info:
        if line not in posted:
            send_message(line)
            posted.add(line)
            time.sleep(1)
    write_posted(posted)

if __name__ == "__main__":
    while True:
        run_bot()
        time.sleep(60)
