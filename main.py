# main.py
from dotenv import dotenv_values
import requests
from notion_client import Client
import httpx
from reports import *

env_vars = dotenv_values(".env")

telegram_bot_token = env_vars["TELEGRAM_BOT_TOKEN"]
telegram_chat_id = env_vars["TELEGRAM_CHAT_ID"]
notion_token = env_vars["NOTION_API_TOKEN"]
notion_page_id = env_vars["NOTION_PAGE_ID"]
notion_db_id = env_vars["NOTION_DB_ID"]

def main():
    try:
        notion = Client(auth=notion_token)
        users_list_response = notion.users.list()
    except:
        notion = Client(auth=notion_token, client=httpx.Client(verify=False))
        users_list_response = notion.users.list()

    # result = report_cesta(notion, notion_db_id, 'Dia 5')
    # send_telegram_message(result)

    # result = report_cesta(notion, notion_db_id, 'Dia 20')
    # send_telegram_message(result)

    # result = report_fralda(notion, notion_db_id, 'Dia 5')
    # send_telegram_message(result)

    # result = report_fralda(notion, notion_db_id, 'Dia 20')
    # send_telegram_message(result)

    result = report_pedencia(notion, notion_db_id, 'Dia 5')
    send_telegram_message(result)

    result = report_pedencia(notion, notion_db_id, 'Dia 20')
    send_telegram_message(result)

def send_telegram_message(message, token=telegram_bot_token, chat_id=telegram_chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(url, json=data)
    except:
        response = requests.post(url, json=data, verify=False)

    if response.status_code != 200:
        print("Failed to send message to Telegram.")
    else:
        print("Message sent successfully!")

if __name__ == '__main__':
    main()