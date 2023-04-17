import asyncio
from config import client, Strings, Config
from telethon.custom import Message
from modules.handlers.limiter import Limit
from modules.handlers.step import Step
from modules.requests_to_api import APIS
from modules.functions.payment_link import create_payment_link
from modules.buttons import TextButtons, UrlButtons

async def get_informatios(event: Message) -> "This function is for handler":

    text = str(event.message.message)
    limit = Limit.LIMIT[str(event.sender_id)]
    if (limit["part"] == Step.GET_CUSTOM_SHARJ):

        if (text.isnumeric()):

            seller = True
            Price = Config.MIN_USER_SHARJ if seller is False else Config.MIN_SELLER_SHARJ
            if (int(text) >= Price):

                await client.send_message(
                    event.chat_id,
                    Strings.WAITING,
                    buttons= TextButtons.start_menu(event.sender_id)
                )
                await asyncio.sleep(0.5)
                link = create_payment_link(event.sender_id, int(text))
                await client.send_message(
                    event.chat_id,
                    Strings.created_payment_link(text),
                    buttons= UrlButtons.payment_link(link)
                )
                text, link, Price = 0, 0, 0
                del Limit.LIMIT[str(event.sender_id)]

            else:

                await client.send_message(
                    event.chat_id,
                    Strings.low_price(Price)
                )

        else:

            await client.send_message(
                event.chat_id,
                Strings.NOT_NUMBER
            )

    elif (limit["part"] == ""):
        ...












