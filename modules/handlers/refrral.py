from config import Config, client, Strings
from modules import TextButtons
async def refrral(event):

    user = str(event.message.message).lower().replace('https://t.me/{}?start='.format(Config.BOT_USERNAME), '')
    CeckUser = ...

    await client.send_message(
        event.chat_id,
        Strings.start_menu(event.chat.first_name, event.sender_id),
        buttons= TextButtons.START_MENU
    )

