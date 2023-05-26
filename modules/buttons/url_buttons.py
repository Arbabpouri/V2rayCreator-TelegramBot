from telethon import Button
from typing import List, Optional
from modules.buttons.inline_buttons import InlineButtonsString
from config import Config
from modules.api.urls import ApiUrls
from modules.api.APIS import APIS




class UrlButtonsString:

    SUPPORT = "📞 ارتباط با ادمین 📞"
    REFERRAL = "💢 لینک زیر مجموعه گیری 💢"
    CLICK_ME = "📍 کلیک کنید 📍"

    @staticmethod
    def shop(price: int) -> str:
        return f"🔋 {int(price):,} تومان 💸"



class UrlButtons:

    SUPPORT = [[Button.url(UrlButtonsString.SUPPORT, "https://t.me/{}".format(Config.ADMIN_USERNAME))]]

    def __init__(self, user_id: int) -> None:
        self.user_id = user_id


    def referral(self) -> List[Button]:
        """_summary_

        Returns:
            List[Button]: _description_
        """

        return [
            [
                Button.url(UrlButtonsString.REFERRAL, f"https://t.me/{Config.BOT_USERNAME}?start={int(self.user_id)}"),
            ],
        ]


    def shop(self, min_price: int | None = None) -> List[Button]:
        """_summary_

        Args:
            min_price (int): _description_

        Returns:
            List[Button]: _description_
        """

        if (min_price is None):
            min_price = APIS.config_api().get_prices_limit

        

        self.user_id = int(self.user_id)
        buttons = [
            [
                Button.url(f"{int(min_price * 1):,} تومان", ""),
                Button.url(f"{int(min_price * 2):,} تومان", "")
            ],
            [
                Button.url(f"{int(min_price * 3):,} تومان", ""),
                Button.url(f"{int(min_price * 4):,} تومان", ""),
            ],
            [
                Button.inline(InlineButtonsString.CUSTOM_CHARGE, "ONLINE-CUSTOM-CHARGE")
            ],
        ]
        
        del (min_price)
        return buttons


    @staticmethod
    def payment_link(link) -> List[Button]:

        """
            
        """

        return [[Button.url(UrlButtonsString.CLICK_ME, link)]]

