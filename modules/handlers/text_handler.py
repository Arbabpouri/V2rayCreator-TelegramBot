from uuid import uuid1
from telethon.custom import Message
from telethon.types import MessageMediaPhoto, PeerChannel
from re import match
from config import client, Config
from config.bot_strings import Strings
from modules.buttons import (TextButtunsString, TextButtons, UrlButtons, InlineButtons)
from modules.handlers.limiter import Limit, Step
from modules.api.APIS import APIS
from modules.api.urls import ApiUrls
from modules.enums import UserTypes
from modules.tools.check_configs import check_config


class TextHandlers:


    @staticmethod
    async def user_move(event: Message) -> None:

        text = str(event.message.message)
        
        if (match(r"^/start [0-9]", text)):

            user_id = str(event.message.message).lower().replace('https://t.me/{}?start='.format(Config.BOT_USERNAME), '')
            user_id = user_id.replace("/start ", "")
            
            APIS.user_api(event.sender_id).add_user(
                referraler=0 if (user_id == str(event.sender_id) or not user_id.isnumeric() or
                                  APIS.user_api(user_id).get_user_type != UserTypes.MANUAL) \
                else int(user_id)
            )

            text = "/start"


        match(text):

            # this is session for /start and send main menu
            case ("/start"):

                add = APIS.user_api(user_id=event.sender_id).add_user()

                if (add):message = Strings.start_menu(event.chat.first_name, event.sender_id)
                else: message = Strings.ERROR

                await client.send_message(
                    event.chat_id,
                    Strings.start_menu(event.chat.first_name, event.sender_id),
                    buttons=TextButtons.start_menu(event.sender_id)
                )
                
            # this is session for select server for buy
            case (TextButtunsString.BUY_CONFIG):

                message, buttons = InlineButtons(event.sender_id).select_server()

                await client.send_message(
                    event.chat_id,
                    message,
                    buttons=buttons
                )

            # this is session for show accounts information
            case (TextButtunsString.ACCOUNT):

                await client.send_message(
                    event.chat_id,
                    Strings.account(event.sender_id),
                )

            # this is session for show configs
            case (TextButtunsString.MY_SUBSCRIPTIONS):

                message, buttons = InlineButtons(int(event.sender_id)).user_configs
                await client.send_message(
                    event.chat_id,
                    message,
                    buttons=buttons
                )
                
            # this is session for show charge buttons
            case (TextButtunsString.SHOP):

                await client.send_message(
                    event.chat_id,
                    Strings.SELECT_CHARGE,
                    buttons=TextButtons.SELECT_CHARGE
                )

            # this is session for online charge
            case (TextButtunsString.ONLINE_CHARGE | TextButtunsString.OFFLINE_CHARGE | TextButtunsString.CRYPTO_CHARGE):

                await client.send_message(
                    event.sender_id,
                    "cheghad?",
                    buttons=TextButtons.CANCEL_GET
                )

                # step
                if (text == TextButtunsString.ONLINE_CHARGE):
                    part = Step.GET_CUSTOM_CHARGE_ONLINE
                elif (text == TextButtunsString.OFFLINE_CHARGE):
                    part = Step.GET_CUSTOM_CHARGE_OFFLINE
                elif (text == TextButtunsString.CRYPTO_CHARGE):
                    part = Step.GET_CUSTOM_CHARGE_CRYPTO

                Limit.LIMIT[str(event.sender_id)] = {
                    "part": part,
                    "last-message": event.message.message,
                }

            # this is session for back to 'TextButtons.start_menu(event.sender_id)'
            case (TextButtunsString.BACK_TO_START_MENU):

                await client.send_message(
                    event.chat_id,
                    Strings.BACKED_TO_HOME,
                    buttons=TextButtons.start_menu(int(event.sender_id))
                )

            # this is session for send referral link to user
            case (TextButtunsString.REFERRAL):

                await client.send_message(
                    event.chat_id,
                    Strings.referral(event.sender_id),
                    buttons=UrlButtons(event.sender_id).referral
                )

            # this is session for send admin username to user
            case (TextButtunsString.SUPPORT):

                await client.send_message(
                    event.chat_id,
                    Strings.SUPPORT,
                    buttons=UrlButtons.SUPPORT
                )

            # this is session for send userid for user
            case (TextButtunsString.GET_USER_ID):

                await client.send_message(
                    event.chat_id,
                    Strings.get_user_id(event.sender_id),
                    parse_mode="html"
                )
            
            #
            case _:
                pass

    @staticmethod
    async def get_informatios(event: Message) -> None:

        if (event.message.message == TextButtunsString.CANCEl_GET):
            
            await client.send_message(
                event.chat_id,
                Strings.CANCELED,
                buttons=TextButtons.start_menu(int(event.sender_id))
            )
            del Limit.LIMIT[str(event.sender_id)]
            return

        informations = Limit.LIMIT[str(event.sender_id)]
        part = informations["part"]

        if (informations["last-message"] == event.message.message): return

        
        

        # get number for payment link for create custom charge
        match(part):

            #this session for get custom charge number
            case (Step.GET_CUSTOM_CHARGE_ONLINE | Step.GET_CUSTOM_CHARGE_OFFLINE | Step.GET_CUSTOM_CHARGE_CRYPTO):

                if (not str(event.message.message).isnumeric()):

                    await client.send_message(event.chat_id, Strings.NOT_NUMBER)

                else:

                    text = int(event.message.message)
                    user_api = APIS.user_api(event.sender_id)
                    user_type = user_api.get_user_type
                    
                    if (isinstance(user_type, bool) and not user_type):

                        await client.send_message(
                            event.chat_id,
                            Strings.ERROR,
                            buttons=TextButtons.start_menu(event.sender_id)
                        )

                        del Limit.LIMIT[str(event.sender_id)]

                    else:

                        if (user_type == UserTypes.MANUAL):
                            min_charge = Config.MIN_USER_CHARGE
                        else:
                            api_config = APIS.config_api()
                            min_charge = api_config.get_prices_limit

                    if (text < min_charge):

                        await client.send_message(
                            event.chat_id,
                            Strings.low_price(min_charge),
                            buttons=TextButtons.CANCEL_GET
                        )

                    else:

                        if (part == Step.GET_CUSTOM_CHARGE_ONLINE):

                            await client.send_message(
                                event.chat_id,
                                Strings.WAITING,
                                buttons=TextButtons.start_menu(event.sender_id)
                            )

                            link = ApiUrls().online_charge(user_id=int(event.sender_id), amount=int(text))

                            await client.send_message(
                                event.chat_id,
                                Strings.created_payment_link(text),
                                buttons=UrlButtons.payment_link(link)
                            )

                            del Limit.LIMIT[str(event.sender_id)]

                        elif (part == Step.GET_CUSTOM_CHARGE_OFFLINE):

                            informations = Limit.LIMIT[str(event.sender_id)] = {
                                "part": Step.GET_EVIDENCE,
                                "price": int(text),
                                "last-message": event.message.message
                            }

                            await client.send_message(
                                event.chat_id,
                                Strings.send_evidence(price=informations["price"]),
                                buttons=TextButtons.CANCEL_GET
                            )

                        elif (part == Step.GET_CUSTOM_CHARGE_CRYPTO):

                            await client.send_message(
                                event.chat_id,
                                Strings.WAITING,
                                buttons=TextButtons.start_menu(event.sender_id)
                            )

                            




                            

                            # TODO. dar in bakhsh bayad link va dokme pardakht kardam ezafe shavad
                            











                            del Limit.LIMIT[str(event.sender_id)]

                        else:

                            await client.send_message(
                                event.chat_id,
                                Strings.ERROR,
                                buttons=TextButtons().start_menu(int(event.sender_id))
                            )

                            del Limit.LIMIT[str(event.sender_id)]


            # this session for get deposit documents
            case (Step.GET_EVIDENCE):



                if (isinstance(event.message.media, MessageMediaPhoto)):

                    del Limit.LIMIT[str(event.sender_id)]

                    await client.send_message(
                        event.chat_id,
                        Strings.DOCUMENTS_RECEIVED,
                        buttons=TextButtons.start_menu(int(event.sender_id)),
                    )

                    photo = event.photo
                    text = Strings.acc_reject(
                        name=str(event.chat.first_name),
                        user_name=str(event.chat.username),
                        user_id=int(event.sender_id),
                        amount=int(informations["price"]),
                    )
                    buttons = InlineButtons(int(event.sender_id)).acc_reject(informations["price"])
                    try:

                        await client.send_file(
                            PeerChannel(Config.ACC_REJECT_CHANNEL_ID),
                            photo,
                            caption=text,
                            buttons=buttons,
                        )

                    except:
                        
                        for admin in Config.ADMINS_USER_ID:

                            try:

                                await client.send_file(
                                    admin,
                                    photo,
                                    caption=text,
                                    buttons=buttons,
                                )
                                break

                            except: pass
                        
                        else:

                            await client.send_message(
                                event.chat_id,
                                Strings.DOCUMENTS_NOT_RECEIVED,
                                buttons=UrlButtons.SUPPORT
                            )

                else:

                    await client.send_message(
                        event.chat_id,
                        Strings.NOT_PICTURE,
                        buttons=TextButtons.CANCEL_GET
                    )

