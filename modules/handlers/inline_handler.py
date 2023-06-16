from telethon.events import CallbackQuery
from telethon.types import PeerUser

from config import client
from config.bot_strings import Strings
from modules.buttons import TextButtons, InlineButtons, UrlButtons, UrlButtonsString
from modules.api.APIS import APIS
from modules.api.urls import ApiUrls
from modules.handlers.limiter import Limit, Step
from modules.enums.enums import ResponseCode, UserTypes, CryptoStatus
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

            # data[0] is the server id
            server_id = data.lstrip("BUY-SELECT-SERVER-").split("-")[0]
            result, buttons = InlineButtons(
                event.sender_id).configs_for_sell(int(server_id))

            await event.edit(
                "select config" if (result) else "not config",
                buttons=buttons
            )

        elif (data.startswith("BUY-CONFIG-")):

            # data[0] is server id and data[1] is config id
            data = data.lstrip("BUY-CONFIG-").split("-")
            server_id, config_id = data
            buttons = InlineButtons().vmess_or_vless(
                server_id=int(server_id),
                config_id=int(config_id),
            )

            await event.edit("test", buttons=buttons)

        elif (data.startswith("BUY-SELECT-PROTOCOL-")):

            # data[0] is protocol, data[1] is server id, data[2] is config id
            data = data.lstrip("BUY-SELECT-PROTOCOL-").split("-")
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
                        response_error = Strings.RESPONSE_API_STRINGS
                        text = response_error[str(add_config)]\
                            if (str(add_config) in list(response_error.keys())) else Strings.ERROR

                    else:

                        text = f"linket `{add_config.v2RayLink}`"

                else:

                    user_api = APIS.user_api(int(event.sender_id))

                    payment_link_irr = ApiUrls().online_buy_config(
                        user_id=int(event.sender_id),
                        server_id=int(server_id),
                        config_type_id=int(config_id)
                    )

                    payment_crypto_informations = user_api.online_crypto_charge_link(toman_amount=price)

                    if (isinstance(payment_link_irr, int) or
                        isinstance(payment_crypto_informations, int)):
                        
                        response_error = list(Strings.RESPONSE_API_STRINGS.keys())

                        if (str(payment_link_irr) in response_error or
                            str(payment_crypto_informations) in response_error):

                            text = Strings.RESPONSE_API_STRINGS[str(payment_link_irr)]

                        else:

                            text = Strings.ERROR
                        
                        buttons = []

                    else:

                        text = Strings.created_payment_link(price=price)
                        crypto_payment_link = ApiUrls().crypto_payment_url(
                            amount=payment_crypto_informations.pay_amount,
                            address=payment_crypto_informations.pay_address
                        )
                        
                        buttons = [
                            
                            UrlButtons.payment_link(payment_link_irr, UrlButtonsString.IRR_PAYMENT),
                            UrlButtons.payment_link(crypto_payment_link, UrlButtonsString.CRYPTO_PAYMENT),
                            InlineButtons(int(event.sender_id)).crypto_status_online(
                                payment_id=payment_crypto_informations.payment_id,
                                amount=payment_crypto_informations.pay_amount,
                                server_id=server_id,
                                config_id=config_id
                            )
                            
                        ]

                await event.edit(
                    text,
                    buttons=buttons
                )

        elif (data.startswith("SHOW-CONFIG-INFO")):

            config_id = data.lstrip("SHOW-CONFIG-INFO-")

            if (not str(config_id).isnumeric()):

                await event.edit(Strings.ERROR, buttons=InlineButtons().BACK_TO_HOME)
                return

            message, buttons = InlineButtons(
                int(event.sender_id)).show_config(int(config_id))
            await event.edit(message, buttons=buttons)

        elif (data.startswith("RENEWAL-CONFIG-")):

            config_id = data.lstrip("RENEWAL-CONFIG-")
            v2ray = APIS.v2ray_api()
            renewal = v2ray.renewal_config(int(config_id))

            if (str(renewal)):
                text = Strings.RESPONSE_API_STRINGS[str(renewal)] if (
                    str(renewal) in Strings.RESPONSE_API_STRINGS.keys()) else Strings.ERROR

            elif (isinstance(renewal, RenewalConfigResult)):
                text = renewal.v2RayLink

            else:
                text = Strings.ERROR

            await event.edit(
                text,
                buttons=InlineButtons().BACK_TO_CONFIGS
            )

        elif (data.startswith("CHANGE-PROTOCOL-")):

            config_id = data.lstrip("CHANGE-PROTOCOL-")

            if (not str(config_id).isnumeric()):

                await event.edit(Strings.ERROR, buttons=InlineButtons().BACK_TO_HOME)
                return

            v2ray = APIS.v2ray_api()
            config = v2ray.change_protocol(int(config_id))

            if (isinstance(config, int)):
                text = Strings.RESPONSE_API_STRINGS[str(change)] if (
                    change in Strings.RESPONSE_API_STRINGS.keys()) else Strings.ERROR

            elif (isinstance(config, ChangeProtocolResult)):
                text = config.v2RayLink

            else:
                text = Strings.ERROR

            await event.edit(text, buttons=InlineButtons().show_config(config_id)[1])

        elif (data.startswith("CHANGE-SERVER-")):

            config_id = data.lstrip("CHANGE-SERVER-")

            if (not str(config_id).isnumeric()):

                await event.edit(Strings.ERROR, buttons=InlineButtons().BACK_TO_HOME)
                return

            message, buttons = InlineButtons(int(event.sender_id)).select_server("CHANGE", int(config_id))
            await event.edit(message, buttons=buttons)

        elif (data.startswith("CHANGE-SELECT-SERVER-")):

            data = data.lstrip("CHANGE-SELECT-SERVER-").split("-")
            server_id, config_id = data

            if (not (str(server_id).isnumeric() or str(server_id).isnumeric())):

                await event.edit(Strings.ERROR, buttons=InlineButtons().BACK_TO_HOME)
                return

            v2ray = APIS.v2ray_api()
            change = v2ray.change_server(int(config_id), int(server_id))

            if (isinstance(change, int)):
                text = Strings.RESPONSE_API_STRINGS[str(change)] if (
                    change in Strings.RESPONSE_API_STRINGS.keys()) else Strings.ERROR

            elif (isinstance(change, ChangeServerResult)):
                text = change.v2RayLink

            else:
                text = Strings.ERROR

            await event.edit(text, buttons=InlineButtons().BACK_TO_HOME)

        elif (data.startswith(("CRYPTO-STATUS-", "CRYPTO-ONLINE-STATUS-"))):

            user_api = APIS.user_api(int(event.sender_id))

            if (data.startswith("CRYPTO-STATUS-")):

                data = data.lstrip("CRYPTO-STATUS-").split("-")
                await event.answer(message=Strings.WAITING, cache_time=1)
                payment_id, amount = data
                
                status = user_api.crypto_status(
                    payment_id=payment_id,
                    crypto_payment_type=0,
                    price=amount
                )

                if (isinstance(status, int)):

                    text = Strings.error_text(status)
                
                else:

                    if (status == CryptoStatus.FINISHED):

                        increase_balance = user_api.balance_increase(how_much=amount)

                        if (increase_balance):
                            
                            text = Strings.PAID
                            await event.delete()
                        
                        else:

                            text = Strings.ERROR

                    else:

                        await event.answer(message=Strings.UNPAIN, cache_time=1, alert=True)
                        return

            else:

                data = data.lstrip("CRYPTO-ONLINE-STATUS-").split("-")
                payment_id, amount, server_id, config_id = data
                
                status = user_api.crypto_status(
                    payment_id=payment_id,
                    crypto_payment_type=1,
                    price=amount
                )

                if (isinstance(status, int)):

                    text = Strings.error_text(status)
                
                else:

                    if (status == CryptoStatus.FINISHED):
                        
                        v2ray = APIS.v2ray_api()
                        add_config = v2ray.add_new_config(
                            user_id=int(event.sender_id),
                            server_id=server_id,
                            config_type_id=config_id,
                            protocol="VMESS",
                            is_free=True
                        )

                        if (isinstance(add_config, int)):

                            text = Strings.error_text(add_config)
                        
                        else:

                            text = Strings.your_config(add_config.v2RayLink)
                            await event.delete()

                    else:

                        await event.answer(message=Strings.UNPAIN, cache_time=1, alert=True)
                        return
            
            await client.send_message(
                entity=event.chat_id,
                message=text
            )
                
                



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
        if (data.__len__() != 3):
            return
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

                except:
                    pass

            else:
                await event.answer(Strings.ACC_ERROR, alert=True)

        elif (action == "reject"):

            await event.edit(Strings.admin_rejected(user_id, event.sender_id, amount))

            try:

                await client.send_message(
                    PeerUser(int(user_id)),
                    Strings.user_rejected(amount)
                )

            except:
                pass
