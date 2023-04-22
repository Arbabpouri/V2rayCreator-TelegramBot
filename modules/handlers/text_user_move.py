from config import client, Strings
from telethon.custom import Message
from modules import TextButtunsString, TextButtons, UrlButtons, APIS


async def user_move(event: Message) -> None:
    text = str(event.message.message)
    match(text):
        # this is session for /start and send main menu
        case ("/start"):
            await APIS.UserApi.add_user(event.sender_id)
            await client.send_message(
                event.chat_id,
                Strings.start_menu(event.chat.first_name, event.sender_id),
                buttons=TextButtons.start_menu(event.sender_id)
            )
        # this is session for select server for buy
        case (TextButtunsString.BUY_CONFIG):
            await client.send_message(
                event.chat_id,
                Strings.BUY_CONFIG,

            )
        # this is session for show accounts information
        case (TextButtunsString.ACCOUNT):
            await client.send_message(
                event.chat_id,
                Strings.account(event.sender_id),
                buttons=TextButtons.start_menu(event.sender_id),
                parse_mode="html"
            )
        # this is session for show configs
        case (TextButtunsString.MY_SUBSCRIPTIONS):
            print(event.message.message)
            print(event.message.message)

        # this is session for show charge buttons
        case (TextButtunsString.SHOP):
            user_type = await APIS.UserApi.get_user_type(event.sender_id)
            if (user_type is False):
                ...
            await client.send_message(
                event.chat_id,
                Strings.SHOP,
                buttons=UrlButtons.shop(event.sender_id, user_type)
            )
        # this is session for send referral link to user
        case (TextButtunsString.REFERRAL):
            await client.send_message(
                event.chat_id,
                Strings.referral(event.sender_id),
                buttons=UrlButtons.referral(event.sender_id)
            )
        # this is session for send admin username to user
        case (TextButtunsString.SUPPORT):
            await client.send_message(
                event.chat_id,
                Strings.SUPPORT,
                buttons=UrlButtons.SUPPORT
            )
        # this is session for send userid for user
        case (TextButtunsString.GET_USER_ID):
            await client.send_message(
                event.chat_id,
                Strings.get_user_id(event.sender_id),
                buttons=TextButtons.start_menu(event.sender_id),
                parse_mode="html"
            )
        case _:
            pass
