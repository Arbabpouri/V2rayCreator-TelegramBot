from config import Config, client, Strings
from modules import TextButtons
from modules import APIS


async def referral_handler(event):


    user_id = str(event.message.message).lower().replace('https://t.me/{}?start='.format(Config.BOT_USERNAME), '')
    # if user == seller or user not found (nothing)
    await APIS.UserApi.add_user(
        user_id=event.sender_id,
        referraler=user_id if (APIS.UserApi.get_user_type(user_id=user_id) not in [0, 1]) else 0
    )
    await client.send_message(
        event.chat_id,
        Strings.start_menu(event.chat.first_name, event.sender_id),
        buttons=TextButtons.start_menu(event.sender_id)
    )
