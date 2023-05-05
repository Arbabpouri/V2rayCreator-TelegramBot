from telethon import Button
from typing import List
from modules.buttons.inline_buttons import InlineButtonsData, InlineButtonsString
from config import Config
from modules.functions import create_payment_link



class UrlButtonsString:

    SUPPORT = "📞 ارتباط با ادمین 📞"
    REFERRAL = "💢 لینک زیر مجموعه گیری 💢"
    CLICK_ME = "📍 کلیک کنید 📍"

    @staticmethod
    def shop(price: int) -> str:
        return f"🔋 {int(price):,} تومان 💸"



class UrlButtons:

    SUPPORT = [[Button.url(UrlButtonsString.SUPPORT, "https://t.me/{}".format(Config.ADMIN_USERNAME))]]
    

    def __init__(self) -> None:
        pass


    @staticmethod
    def referral(user_id: int) -> List[Button]:
        return [
            [
                Button.url(UrlButtonsString.REFERRAL, f"https://t.me/{Config.BOT_USERNAME}?start={user_id}")
            ],
        ]


    @staticmethod
    def shop(user_id: int, seller: bool) -> List[Button]:

        price = Config.USER_CHARGE if not seller else Config.SELLER_CHARGE

        buttons = []
        for i in range(0, len(price) - 1, 2):

            buttons.append(
                [
                    Button.url(UrlButtonsString.shop(price[i]), create_payment_link(user_id, price[i])),
                    Button.url(UrlButtonsString.shop(price[i + 1]), create_payment_link(user_id, price[i + 1]))
                ]
            )

        if len(price) % 2 != 0:

            buttons.append(
                [
                    Button.url(UrlButtonsString.shop(price[-1]), create_payment_link(user_id, price[-1]))
                ]
            )

        buttons.append(
            [
                Button.inline(InlineButtonsString.CUSTOM_CHARGE, InlineButtonsData.CUSTOM_CHARGE)
            ]
        )

        return buttons


    @staticmethod
    def payment_link(link) -> List[Button]:
        return [
            [
                Button.url(UrlButtonsString.CLICK_ME, link)
            ]
        ]
