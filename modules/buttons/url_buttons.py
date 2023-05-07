from telethon import Button
from typing import List
from modules.buttons.inline_buttons import InlineButtonsData, InlineButtonsString
from config import Config
from modules.tools import create_payment_link



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
        """
        
        """

        return [
            [
                Button.url(UrlButtonsString.REFERRAL, f"https://t.me/{Config.BOT_USERNAME}?start={user_id}"),
            ],
        ]


    @staticmethod
    def shop(user_id: int, min_price: int) -> List[Button]:
        """

        """
        
        if (not str(user_id).isnumeric() or not str(min_price).isnumeric()):
            raise ValueError("user_id/min_price argument must be number")
        
        user_id = int(user_id)
        price = int(min_price)
        buttons = [
            [
                Button.url(UrlButtonsString.shop(price), create_payment_link(user_id, price)),
                Button.url(UrlButtonsString.shop(price * 2), create_payment_link(user_id, price * 2)),
            ],
            [
                Button.url(UrlButtonsString.shop(price * 3), create_payment_link(user_id, price * 3)),
                Button.url(UrlButtonsString.shop(price * 4), create_payment_link(user_id, price * 4)),
            ],
            [
                Button.inline(InlineButtonsString.CUSTOM_CHARGE, InlineButtonsData.CUSTOM_CHARGE)
            ],
        ]

        del (user_id, price)
        return buttons


    @staticmethod
    def payment_link(link) -> List[Button]:

        """
            
        """

        return [[Button.url(UrlButtonsString.CLICK_ME, link)]]
