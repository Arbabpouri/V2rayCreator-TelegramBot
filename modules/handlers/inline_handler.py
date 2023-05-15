from config import client, Strings
from modules import TextButtons, OfflineChargeData, APIS
from modules.handlers.limiter import Limit, Step
from telethon.events import CallbackQuery
from typing import NoReturn


class InlineHandlers:


    @staticmethod
    async def inline_set_part(event: CallbackQuery.Event) -> NoReturn:
        data = bytes(event.data).decode()
        if (data == "CUSTOM-CHARGE"):
            await client.send_message(
                event.chat_id,
                Strings.GET_CUSTOM_CHARGE,
                buttons=TextButtons.CANCEL_GET
            )
            Limit.LIMIT[str(event.sender_id)] = {
                "part": Step.GET_CUSTOM_CHARGE_ONLINE
            }


    @staticmethod
    async def acc_reject(event: CallbackQuery.Event) -> NoReturn:
        data = bytes(event.data).decode()
        if (data.startswith("acc-")):
            data = data.replace("acc-", "")
            delete = OfflineChargeData(data).delete(event.sender_id, "accepted")
            if (delete):
                price = OfflineChargeData(data).read()
                price = price["price"]

            else:
                pass

        elif (data.startswith("reject-")):
            data = data.replace("reject-", "")
            delete = OfflineChargeData(data).delete(event.sender_id, "failed")
            if (delete):
                pass
            else:
                pass
