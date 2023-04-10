from telethon import TelegramClient
from config import Config

try:

    client = TelegramClient(
        session= Config.SESSION_NAME,
        api_id= Config.API_ID,
        api_hash= Config.API_HASH
    )

    client.start(bot_token= Config.BOT_TOKEN)

except Exception as ex:
    print(ex)