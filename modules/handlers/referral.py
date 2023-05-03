from config import Config, client, Strings
from modules import TextButtons
from modules import APIS


async def referral_handler(event):

    user_id = str(event.message.message).lower().replace('https://t.me/{}?start='.format(Config.BOT_USERNAME), '')

    await APIS.user_api(event.sender_id).add_user(
        referraler=0 if (user_id == str(event.sender_id) or not user_id.isnumeric() or APIS.user_api(user_id).get_user_type in [1, 2]) \
        else int(user_id)
    )

    await client.send_message(
        event.chat_id,
        Strings.start_menu(event.chat.first_name, event.sender_id),
        buttons=TextButtons.start_menu(event.sender_id)
    )

    del user_id
