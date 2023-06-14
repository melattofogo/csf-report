
The ```main``` code initializes the Notion client, generates reports using the functions from the ```reports``` module, and sends the reports to a Telegram chat using the ```send_telegram_message``` function. The environment variables are loaded from a ```.env``` file, and the Telegram bot token, chat ID, Notion API token, Notion page ID, and Notion database ID are extracted from the environment variables. The ```main``` function is called when the script is executed, triggering the generation and sending of reports.

```.env``` example:

```
TELEGRAM_BOT_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TELEGRAM_CHAT_ID="xxxxxxxxxx"
NOTION_API_TOKEN="secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
NOTION_PAGE_ID="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
NOTION_DB_ID="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
NOTION_DB_PAGE_ID="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
