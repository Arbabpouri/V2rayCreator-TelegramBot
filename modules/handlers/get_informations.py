import asyncio
from config import client, Strings, Config
from telethon.custom import Message
from modules.handlers.limiter import Limit, Step
from modules.requests_to_api import APIS
from modules.functions.payment_link import create_payment_link
from modules.buttons import TextButtons, UrlButtons

async def get_informatios(event: Message) -> None:
    text = str(event.message.message)
    limit = Limit.LIMIT[str(event.sender_id)]

    # get number for payment link for create custom charge
    match(limit["part"]):

        case (Step.GET_CUSTOM_CHARGE):
    
            if (not text.isnumeric()):
                await client.send_message(event.chat_id, Strings.NOT_NUMBER)

            else:
                text = int(text)
                user_type = await APIS.user_api(event.sender_id).get_user_type
                # if user founded
                if (user_type != 2):
                    Price = Config.MIN_USER_CHARGE if (user_type == 0) else Config.MIN_SELLER_CHARGE
                    if (text >= Price):
                        await client.send_message(
                            event.chat_id,
                            Strings.WAITING,
                            buttons=TextButtons.start_menu(event.sender_id)
                        )
                        await asyncio.sleep(0.5)
                        link = create_payment_link(event.sender_id, text)
                        await client.send_message(
                            event.chat_id,
                            Strings.created_payment_link(text),
                            buttons=UrlButtons.payment_link(link)
                        )
                        del (Limit.LIMIT[str(event.sender_id)], text, link, Price)

                    else:
                        await client.send_message(event.chat_id, Strings.low_price(Price))

    
