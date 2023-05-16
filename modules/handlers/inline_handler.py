from config import client, Strings
from modules import TextButtons, OfflineChargeData, APIS
from modules.handlers.limiter import Limit, Step
from telethon.events import CallbackQuery
from typing import NoReturn
from modules.models.models import OfflineCharge


class InlineHandlers:


    @staticmethod
    async def inline_set_part(event: CallbackQuery.Event) -> NoReturn:
        """_summary_

        Args:
            event (CallbackQuery.Event): _description_

        Returns:
            NoReturn: _description_
        """
        
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
        """
        acc or reject by admin

        Args:
            event (CallbackQuery.Event): _description_

        Returns:
            NoReturn: _description_
        """

        callback_data = bytes(event.data).decode()
        if (callback_data.startswith("acc-")):

            id = callback_data.replace("acc-", "")
            delete = OfflineChargeData(id).delete(event.sender_id, "accepted")
            if (delete):

                data = OfflineChargeData(id).read()
                price = OfflineCharge(**price)
                balance_increase = APIS.user_api(price.user_id).balance_increase()
                if (balance_increase):

                    await client.send_message(
                        event.chat_id,
                        "s"
                    )

                else:
                    
                    await client.send_message(
                        event.chat_id,
                        "s"
                    )
                
                del (callback_data, id, delete, data, price, balance_increase)
                return
                
            else:

                await client.send_message(
                    event.chat_id,
                    "s"
                )
                del (callback_data, id, delete)

        elif (callback_data.startswith("reject-")):

            id = callback_data.replace("reject-", "")
            delete = OfflineChargeData(id).delete(event.sender_id, "failed")
            if (delete):

                pass

            else:

                pass
        
