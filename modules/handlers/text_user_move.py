from config import client, Strings
from telethon.custom import Message
from modules import TextButtunsString, TextButtons, UrlButtons



async def user_move(event: Message) -> None:
    text = str(event.message.message)

    # in bakhsh /start ve ersal menu asli bot ast
    if text == "/start":

        await client.send_message(
            event.chat_id,
            Strings.start_menu(event.chat.first_name, event.sender_id),
            buttons= TextButtons.START_MENU
        )

    # in bakhsh enteghab server ast baraye kharid
    elif text == TextButtunsString.BUY_CONFIG:

        await client.send_message(
            event.chat_id,
            Strings.BUY_CONFIG,

        )

    # in bakhsh moshahede moshakhasat ast
    elif text == TextButtunsString.ACCOUNT:

        await client.send_message(
            event.chat_id,
            Strings.account(event.sender_id),
            buttons= TextButtons.START_MENU,
            parse_mode= "html"
        )

    # in bakhsh namayesh eshterak haye karbar ast
    elif text == TextButtunsString.MY_SUBSCRIPTIONS:
        print(event.message.message)
        print(event.message.message)

    # in bakhsh ersal dokme haye sharj ast
    elif text == TextButtunsString.SHOP:

        Seller = False
        await client.send_message(
            event.chat_id,
            Strings.SHOP,
            buttons= UrlButtons.shop(event.sender_id, Seller)
        )

    # in bakhsh ersal link refrral ast
    elif text == TextButtunsString.REFRRAL:

        await client.send_message(
            event.chat_id,
            Strings.refrral(event.sender_id),
            buttons= UrlButtons.refrral(event.sender_id)
        )

    # in bakhsh ersal id postiban ast
    elif text == TextButtunsString.SUPPORT:

        await  client.send_message(
            event.chat_id,
            Strings.SUPPORT,
            buttons= UrlButtons.SUPPORT
        )

    # in bakhsh daryaft id adadi ast
    elif text == TextButtunsString.GET_USER_ID:

        await client.send_message(
            event.chat_id,
            Strings.get_user_id(event.sender_id),
            buttons= TextButtons.START_MENU,
            parse_mode= "html"
        )


