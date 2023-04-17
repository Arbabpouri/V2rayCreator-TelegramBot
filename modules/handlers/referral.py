from config import Config, client, Strings
from modules import TextButtons
from modules import APIS


async def referral_handler(event):

    user = str(event.message.message).lower().replace('https://t.me/{}?start='.format(Config.BOT_USERNAME), '')
    CeckUser = ...

    await client.send_message(
        event.chat_id,
        Strings.start_menu(event.chat.first_name, event.sender_id),
        buttons=TextButtons.start_menu(event.sender_id)
    )

    if (not APIS.is_seller(event.sender_id)):
        pass

