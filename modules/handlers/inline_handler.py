from config import client, Strings
from modules.buttons import TextButtons, InlineButtons
from modules.tools.save_offline_charge import OfflineChargeData
from modules.api.APIS import APIS
from modules.handlers.limiter import Limit, Step
from telethon.events import CallbackQuery
from typing import NoReturn
from modules.models.api_response import OfflineCharge
from enums.response_code import ResponseCode

# TODO
class InlineHandlers:
        

    @staticmethod
    async def user_move(event: CallbackQuery.Event) -> NoReturn:
        """_summary_

        Args:
            event (CallbackQuery.Event): _description_

        Returns:
            NoReturn: _description_
        """
        
        data = bytes(event.data).decode()
        if (data == "CUSTOM-CHARGE"):

            await client.send_message(event.chat_id,
                                      Strings.GET_CUSTOM_CHARGE,
                                      buttons=TextButtons.CANCEL_GET)
            
            Limit.LIMIT[str(event.sender_id)] = {
                "part": Step.GET_CUSTOM_CHARGE_ONLINE
            }
            del data

        elif (data == "BACK-TO-HOME"):

            await client.send_message(entity=event.chat_id,
                                      message=Strings.BACKED_TO_HOME,
                                      buttons=TextButtons.start_menu(event.sender_id))

        elif (data.startswith("SERVER-")):
            
            server_id = data.replace("SERVER-", "")  # data[0] is the server id
            result, buttons = InlineButtons(event.sender_id).configs_for_sell(int(server_id))
                
            await event.edit(message="select config" if (result) else "na",
                             buttons=buttons)

            del (data, buttons, server_id)

        elif (data.startswith("BUY-CONFIG-")):
            
            data = data.replace("BUY-CONFIG-", "").split("-")  # data[0] is server id and data[1] is config id
            server_id, config_id = data
            buttons = InlineButtons().vmess_or_vless(
                server_id=int(server_id),
                config_id=int(config_id),
            )

            await event.edit("test", buttons=buttons)

            del (data, server_id, config_id, price, buttons)

        elif (data.startswith("SELECT-PROTOCOL-")):

            data = data.replace("SELECT-PROTOCOL-", "").split("-")  # data[0] is protocol, data[1] is server id, data[2] is config id
            protocol, server_id, config_id = data
            balance = APIS.user_api(event.sender_id).get_user_information.balance
            price = APIS.v2ray_api().get_config(int(config_id))
            
            if (isinstance(price, int)):

                pass

            else:

                pass



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
        
