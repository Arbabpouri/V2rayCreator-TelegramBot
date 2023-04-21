import asyncio
from config import client, Strings, Config
from telethon.custom import Message
from modules.handlers.limiter import Limit
from modules.handlers.step import Step
from modules.requests_to_api import APIS
from modules.functions.payment_link import create_payment_link
from modules.buttons import TextButtons, UrlButtons

async def get_informatios(event: Message) -> None:
    text = str(event.message.message)
    limit = Limit.LIMIT[str(event.sender_id)]

    # get number for payment link for create custom charge
    if (limit["part"] == Step.GET_CUSTOM_CHARGE):
        if (not text.isnumeric()):
            await client.send_message(event.chat_id, Strings.NOT_NUMBER)

        else:
            user_type = await APIS.UserApi.get_user_type(event.sender_id)
            # if user founded
            if (seller != 3):
                Price = Config.MIN_USER_CHARGE if (user_type == 1) else Config.MIN_SELLER_CHARGE
                if (int(text) >= Price):
                    await client.send_message(
                        event.chat_id,
                        Strings.WAITING,
                        buttons=TextButtons.start_menu(event.sender_id)
                    )
                    await asyncio.sleep(0.5)
                    link = create_payment_link(event.sender_id, int(text))
                    await client.send_message(
                        event.chat_id,
                        Strings.created_payment_link(text),
                        buttons=UrlButtons.payment_link(link)
                    )
                    del Limit.LIMIT[str(event.sender_id)], text, link, Price

                else:
                    await client.send_message(event.chat_id, Strings.low_price(Price))

            # user not found
            else:
                status = await APIS.UserApi.add_user(event.sender_id)

            #     if (status is False):
            #
            #         await client.send_message(event.sender_id, "")
            #         del status
            #         del seller
            #         del limit
            #         del text
            #         del Limit.LIMIT[str(event.sender_id)]
            #         return None
            #         del Limit.LIMIT[str(event.sender_id)], text, link, Price
