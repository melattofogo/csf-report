# main.py
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

telegram_bot_token = env_vars["TELEGRAM_BOT_TOKEN"]
telegram_chat_id = env_vars["TELEGRAM_CHAT_ID"]

def main():
    print(telegram_bot_token)
    print(telegram_chat_id)

if __name__ == '__main__':
    main()