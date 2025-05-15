# GOLDROOT Auto Info Bot

Simple Telegram bot that posts messages from `info.txt` to a Telegram group using `TELEGRAM_BOT_TOKEN` and `CHAT_ID`.

### How it works:
- Add messages to `info.txt`
- Bot will post them (once) to your group
- Sent messages are logged in `posted.txt`

### Deploy Instructions:
1. Deploy on Railway
2. Add 2 variables:
   - TELEGRAM_BOT_TOKEN
   - CHAT_ID
3. Bot will check `info.txt` every 60 seconds and send new lines

Created for the GOLDROOT project.
