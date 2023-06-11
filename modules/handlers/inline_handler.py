from telethon.events import CallbackQuery
from telethon.types import PeerUser

from config import client
from config.bot_strings import Strings
from modules.buttons import TextButtons, InlineButtons
from modules.api.APIS import APIS
from modules.handlers.limiter import Limit, Step
from modules.models.api_response import OfflineCharge
from modules.enums import ResponseCode
from modules.enums import UserTypes
from config import Config
from modules.models.api_response import (
    ChangeProtocolResult,
    ChangeServerResult,
    RenewalConfigResult
)



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

            await client.send_message(
                event.chat_id,
                Strings.GET_CUSTOM_CHARGE,
                buttons=TextButtons.CANCEL_GET
            )
            
            Limit.LIMIT[str(event.sender_id)] = {
                "part": Step.GET_CUSTOM_CHARGE_ONLINE
            }

        elif (data == "BACK-TO-CONFIG-LIST"):

            message, buttons = InlineButtons(int(event.sender_id)).user_configs
            await event.edit(
                message,
                buttons=buttons
            )

        elif (data == "BACK-TO-HOME"):

            await event.edit(
                Strings.BACKED_TO_HOME,
                buttons=TextButtons.start_menu(event.sender_id)
            )

        elif (data.startswith("BUY-SELECT-SERVER-")):
            
            server_id = data.replace("BUY-SELECT-SERVER-", "").split("-")[0]  # data[0] is the server id
            result, buttons = InlineButtons(event.sender_id).configs_for_sell(int(server_id))
                
            await event.edit(
                "select config" if (result) else "not config",
                buttons=buttons
            )

        elif (data.startswith("BUY-CONFIG-")):
            
            data = data.replace("BUY-CONFIG-", "").split("-")  # data[0] is server id and data[1] is config id
            server_id, config_id = data
            buttons = InlineButtons().vmess_or_vless(
                server_id=int(server_id),
                config_id=int(config_id),
            )

            await event.edit("test", buttons=buttons)

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

                        await event.edit("shoma bazaryabi nemituni bekhari", buttons=InlineButtons().BACK_TO_HOME)
                        return
                
                else:

                    await event.edit("config not dound", buttons=InlineButtons().BACK_TO_HOME)
                    return

                if (balance >= price):
                    
                    v2ray = APIS.v2ray_api()

                    add_config = v2ray.add_new_config(
                        user_id=int(event.sender_id),
                        server_id=int(server_id),
                        config_type_id=int(config_id),
                        protocol=protocol.lower(),
                        is_free=False if (not event.sender_id in Config.ADMINS_USER_ID) else True
                    )
                    
                    if (isinstance(add_config, int)):
                        text = Strings.RESPONSE_API_STRINGS[str(payment_link)]\
                            if (str(add_config) in list(Strings.RESPONSE_API_STRINGS.keys())) else Strings.ERROR

                    else:

                        text = f"linket `{add_config.v2RayLink}`"

                else:

                    user_api = APIS.user_api(int(event.sender_id))
                    payment_link = user_api.online_buy_link(
                        server_id=int(server_id),
                        config_id=int(config_id)
                    )

                    if isinstance(payment_link, int):
                        
                        if (str(payment_link) in list(Strings.RESPONSE_API_STRINGS.keys())):

                            text = Strings.RESPONSE_API_STRINGS[str(payment_link)]

                        else:
                            
                            text = "error"
                    
                    else:

                        text = f"linket: {payment_link.result}"

                await event.edit(text, buttons=InlineButtons().BACK_TO_HOME)
                del (text)

        elif (data.startswith("SHOW-CONFIG-INFO")):

            config_id = data.replace("SHOW-CONFIG-INFO-", "")

            if (not str(config_id).isnumeric()):

                await event.edit(Strings.ERROR, buttons=InlineButtons().BACK_TO_HOME)
                return

            message, buttons = InlineButtons(int(event.sender_id)).show_config(int(config_id))
            await event.edit(message, buttons=buttons)

        elif (data.startswith("RENEWAL-CONFIG-")):

            config_id = data.replace("RENEWAL-CONFIG-", "")
            v2ray = APIS.v2ray_api()
            renewal = v2ray.renewal_config(int(config_id))

            if (str(renewal)): text = Strings.RESPONSE_API_STRINGS[str(renewal)] if (str(renewal) in Strings.RESPONSE_API_STRINGS.keys()) else Strings.ERROR

            elif (isinstance(renewal, RenewalConfigResult)): text = renewal.v2RayLink

            else: text = Strings.ERROR

            await event.edit(
                text, 
                buttons=InlineButtons().BACK_TO_CONFIGS
            )
     
        elif (data.startswith("CHANGE-PROTOCOL-")):

            config_id = data.replace("CHANGE-PROTOCOL-", "")

            if (not str(config_id).isnumeric()):
                
                await event.edit(Strings.ERROR, buttons=InlineButtons().BACK_TO_HOME)
                return
            
            v2ray = APIS.v2ray_api()
            config = v2ray.change_protocol(int(config_id))

            if (isinstance(config, int)): text = Strings.RESPONSE_API_STRINGS[str(change)] if (change in Strings.RESPONSE_API_STRINGS.keys()) else Strings.ERROR

            elif (isinstance(config, ChangeProtocolResult)): text = config.v2RayLink

            else: text = Strings.ERROR

            await event.edit(text, buttons=InlineButtons().show_config(config_id)[1])

        elif (data.startswith("CHANGE-SERVER-")):

            config_id = data.replace("CHANGE-SERVER-", "")

            if (not str(config_id).isnumeric()):

                await event.edit(Strings.ERROR, buttons=InlineButtons().BACK_TO_HOME)
                return
            
            message, buttons = InlineButtons(int(event.sender_id)).select_server("CHANGE", int(config_id))
            await event.edit(message, buttons=buttons)
            del (message, buttons, config_id)

        elif (data.startswith("CHANGE-SELECT-SERVER-")):

            data = data.replace("CHANGE-SELECT-SERVER-", "").split("-")
            server_id, config_id = data

            if (not (str(server_id).isnumeric() or str(server_id).isnumeric())):

                await event.edit(Strings.ERROR, buttons=InlineButtons().BACK_TO_HOME)
                return
            
            v2ray = APIS.v2ray_api()
            change = v2ray.change_server(int(config_id), int(server_id))

            if (isinstance(change, int)): text = Strings.RESPONSE_API_STRINGS[str(change)] if (change in Strings.RESPONSE_API_STRINGS.keys()) else Strings.ERROR
            
            elif (isinstance(change, ChangeServerResult)): text = change.v2RayLink

            else: text = Strings.ERROR

            await event.edit(text, buttons=InlineButtons().BACK_TO_HOME)
                

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
        data = callback_data.split("-")
        if (data.__len__() != 3): return
        action, user_id, amount = data

        if (action == "acc"):

            user_id, amount = callback_data.replace("acc-", "").split("-")
            user_api = APIS.user_api(int(event.sender_id))
            increase = user_api.balance_increase(int(amount))

            if (increase):

                await event.edit(
                    Strings.admin_accepted(
                        int(user_id),
                        int(event.sender_id),
                        int(amount)
                    )
                )

                try:

                    await client.send_message(
                        PeerUser(int(user_id)),
                        Strings.user_accepted(amount),
                    )

                except: pass

            else: await event.answer(Strings.ACC_ERROR, alert=True)

        elif (action == "reject"):

            await event.edit(Strings.admin_rejected(user_id, event.sender_id, amount))

            try:

                await client.send_message(
                    PeerUser(int(user_id)),
                    Strings.user_rejected(amount)
                )

            except: pass
