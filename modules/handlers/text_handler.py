from asyncio import sleep
from telethon.custom import Message
from modules.functions.payment_link import create_payment_link
from config import client, Strings, Config
from modules import TextButtunsString, TextButtons, UrlButtons, APIS
from modules.handlers.limiter import Limit, Step


class TextHandlers:


    @staticmethod
    async def user_move(event: Message) -> None:
        text = str(event.message.message)
        match(text):

            # this is session for referral
            case (r"^/start [0-9]"):

                user_id = str(event.message.message).lower().replace('https://t.me/{}?start='.format(Config.BOT_USERNAME), '')

                await APIS.user_api(event.sender_id).add_user(
                    referraler=0 if (user_id == str(event.sender_id) or not user_id.isnumeric() or APIS.user_api(user_id).get_user_type in [1, 2]) \
                    else int(user_id)
                )

                await client.send_message(
                    event.chat_id,
                    Strings.start_menu(event.chat.first_name, event.sender_id),
                    buttons=TextButtons.start_menu(event.sender_id)
                )

                del user_id

            # this is session for /start and send main menu
            case ("/start"):

                await APIS.user_api(user_id=event.sender_id).add_user()
                await client.send_message(
                    event.chat_id,
                    Strings.start_menu(event.chat.first_name, event.sender_id),
                    buttons=TextButtons.start_menu(event.sender_id)
                )
                
            # this is session for select server for buy
            case (TextButtunsString.BUY_CONFIG):

                await client.send_message(
                    event.chat_id,
                    Strings.BUY_CONFIG,

                )

            # this is session for show accounts information
            case (TextButtunsString.ACCOUNT):

                await client.send_message(
                    event.chat_id,
                    Strings.account(event.sender_id),
                    buttons=TextButtons.start_menu(event.sender_id),
                    parse_mode="html"
                )

            # this is session for show configs
            case (TextButtunsString.MY_SUBSCRIPTIONS):
                print(event.message.message)
                print(event.message.message)

            # this is session for show charge buttons
            case (TextButtunsString.SHOP):

                await client.send_message(
                    event.chat_id,
                    Strings.SELECT_CHARGE,
                    buttons=TextButtons().SELECT_CHARGE
                )

            # this is session for online charge
            case (TextButtunsString.ONLINE_CHARGE):
                user_type = await APIS.user_api(user_id=event.sender_id).get_user_type
                await client.send_message(
                    event.chat_id,
                    Strings.SHOP,
                    buttons=UrlButtons.shop(event.sender_id, user_type)
                )
                del user_type

            # this is session for offline charge
            case (TextButtunsString.OFFLINE_CHARGE):
                await client.send_message(
                    event.chat_id,
                    Strings.GET_CUSTOM_CHARGE,
                    # buttons=
                )

            # this is session for send referral link to user
            case (TextButtunsString.REFERRAL):

                await client.send_message(
                    event.chat_id,
                    Strings.referral(event.sender_id),
                    buttons=UrlButtons.referral(event.sender_id)
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
                    buttons=TextButtons.start_menu(event.sender_id),
                    parse_mode="html"
                )
                
            case _:
                pass

    @staticmethod
    async def get_informatios(event: Message) -> None:
        text = str(event.message.message)
        limit = Limit.LIMIT[str(event.sender_id)]

        # get number for payment link for create custom charge
        match(limit["part"]):

            case (Step.GET_CUSTOM_CHARGE_ONLINE):
        
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
                            await sleep(0.5)
                            link = create_payment_link(event.sender_id, text)
                            await client.send_message(
                                event.chat_id,
                                Strings.created_payment_link(text),
                                buttons=UrlButtons.payment_link(link)
                            )
                            del (Limit.LIMIT[str(event.sender_id)], text, link, Price)

                        else:
                            await client.send_message(event.chat_id, Strings.low_price(Price))

        
            case _:
                pass
