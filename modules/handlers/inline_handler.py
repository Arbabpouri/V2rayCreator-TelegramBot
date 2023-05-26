from config import client
from config.bot_strings import Strings
from modules.buttons import TextButtons, InlineButtons
from modules.tools.save_offline_charge import OfflineChargeData
from modules.api.APIS import APIS
from modules.handlers.limiter import Limit, Step
from telethon.events import CallbackQuery
from modules.models.api_response import OfflineCharge
from modules.enums import ResponseCode
from modules.enums import UserTypes
from config import Config

# TODO
class InlineHandlers:
        

    @staticmethod
    async def user_move(event: CallbackQuery.Event) -> None:
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

        elif (data.startswith("SELECT-SERVER-")):
            
            server_id = data.replace("SELECT-SERVER-", "")  # data[0] is the server id
            result, buttons = InlineButtons(event.sender_id).configs_for_sell(int(server_id))
                
            await event.edit(message="select config" if (result) else "not config",
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

        elif (data.startswith("BUY-SELECT-PROTOCOL-")):

            data = data.replace("BUY-SELECT-PROTOCOL-", "").split("-")  # data[0] is protocol, data[1] is server id, data[2] is config id
            protocol, server_id, config_id = data
            user_api = APIS.user_api(event.sender_id)
            balance = user_api.get_user_information.balance
            configs = APIS.v2ray_api().get_all_config_types
            
            if (isinstance(configs, int) and
                configs == ResponseCode.FAILURE):

                await event.edit("get configs error", buttons=InlineButtons().BACK_TO_HOME)

            else:

                for config in configs:

                    if (int(config.id) == int(config_id)):

                        user_type = user_api.get_user_type

                        if (user_type != UserTypes.MARKETER):

                            price = config.priceForManualUsers if (user_type == UserTypes.MANUAL) else \
                                config.priceForSellerUsers
                            
                            break

                        else:

                            await event.edit("shoma bazaryabi nemituni bekhari", buttons=InlineButtons().BACK_TO_HOME)
                            return
                
                else:

                    await event.edit("config not dound", buttons=InlineButtons().BACK_TO_HOME)
                    return

                text = ""

                if (balance >= price):
                    
                    v2ray = APIS.v2ray_api()
                    add_config = v2ray.add_new_config(user_id=int(event.sender_id),
                                                      server_id=int(server_id),
                                                      config_type_id=int(config_id),
                                                      protocol=protocol,
                                                      is_free=False if (event.sender_id not in Config.ADMINS_USER_ID) else True)
                    
                    if (isinstance(add_config, int)):
                        
                        if (str(payment_link) in list(Strings.RESPONSE_API_STRINGS.keys())):

                            text = Strings.RESPONSE_API_STRINGS[str(payment_link)]

                        else:
                            
                            text = "error"

                    else:

                        text = f"linket `{add_config.v2RayLink}`"

                    del (v2ray, add_config)

                else:

                    user_api = APIS.user_api(int(event.sender_id))
                    payment_link = user_api.online_buy_link(server_id=int(server_id),
                                                            config_id=int(config_id))

                    if isinstance(payment_link, int):
                        
                        if (str(payment_link) in list(Strings.RESPONSE_API_STRINGS.keys())):

                            text = Strings.RESPONSE_API_STRINGS[str(payment_link)]

                        else:
                            
                            text = "error"
                    
                    else:

                        text = f"linket: {payment_link.result}"

                    del (user_api, payment_link)

                await event.edit(text, buttons=InlineButtons().BACK_TO_HOME)
                del (text)

    @staticmethod
    async def acc_reject(event: CallbackQuery.Event) -> None:
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
