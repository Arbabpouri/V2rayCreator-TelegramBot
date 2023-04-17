from config import client, Strings
from telethon.custom import Message
from modules import TextButtunsString, TextButtons, UrlButtons


async def user_move(event: Message) -> None:
    text = str(event.message.message)

    # this is session for /start and send main menu
    if (text == "/start"):

        await client.send_message(
            event.chat_id,
            Strings.start_menu(event.chat.first_name, event.sender_id),
            buttons=TextButtons.start_menu(event.sender_id)
        )

    # this is session for select server for buy
    elif (text == TextButtunsString.BUY_CONFIG):

        await client.send_message(
            event.chat_id,
            Strings.BUY_CONFIG,

        )

    # this is session for show accounts information
    elif (text == TextButtunsString.ACCOUNT):

        await client.send_message(
            event.chat_id,
            Strings.account(event.sender_id),
            buttons=TextButtons.start_menu(event.sender_id),
            parse_mode="html"
        )

    # this is session for show configs
    elif (text == TextButtunsString.MY_SUBSCRIPTIONS):
        print(event.message.message)
        print(event.message.message)

    # this is session for show charge buttons
    elif (text == TextButtunsString.SHOP):

        seller = False
        await client.send_message(
            event.chat_id,
            Strings.SHOP,
            buttons=UrlButtons.shop(event.sender_id, seller)
        )

    # this is session for send referral link to user
    elif (text == TextButtunsString.REFERRAL):

        await client.send_message(
            event.chat_id,
            Strings.referral(event.sender_id),
            buttons=UrlButtons.referral(event.sender_id)
        )

    # this is session for send admin username to user
    elif (text == TextButtunsString.SUPPORT):

        await client.send_message(
            event.chat_id,
            Strings.SUPPORT,
            buttons=UrlButtons.SUPPORT
        )

    # this is session for send userid for user
    elif (text == TextButtunsString.GET_USER_ID):

        await client.send_message(
            event.chat_id,
            Strings.get_user_id(event.sender_id),
            buttons=TextButtons.start_menu(event.sender_id),
            parse_mode="html"
        )
