from telethon import Button
from typing import List, Optional, Tuple
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

    SUPPORT = [Button.url(UrlButtonsString.SUPPORT, f"https://t.me/{Config.ADMIN_USERNAME}")]

    def __init__(self, user_id: int) -> None:

        self.user_id = user_id


    @property
    def referral(self) -> List[Button]:
        """_summary_

        Returns:
            List[Button]: _description_
        """

        return [Button.url(UrlButtonsString.REFERRAL, f"https://t.me/{Config.BOT_USERNAME}?start={self.user_id}")]

    
    @staticmethod
    def payment_link(link: str) -> List[Button]:

        """
            
        """

        return [Button.url(UrlButtonsString.CLICK_ME, link)]



    # def shop(self, min_price: Optional[int] = Config.MIN_USER_CHARGE) -> Tuple[str, List[List[Button]]]:
    #     """_summary_

    #     Args:
    #         min_price (Optional[int], optional): _description_. Defaults to Config.MIN_USER_CHARGE.

    #     Returns:
    #         List[Button]: _description_
    #     """

    #     user_api = APIS.user_api(self.user_id)
        
    #     if (min_price is None):
    #         min_price = APIS.config_api().get_prices_limit
        
    #     if (not min_price): min_price = Config.MIN_USER_CHARGE

    #     self.user_id = int(self.user_id)
    #     buttons = [
    #         [
    #             Button.url(f"{int(min_price * 1):,} تومان", ""),
    #             Button.url(f"{int(min_price * 2):,} تومان", "")
    #         ],
    #         [
    #             Button.url(f"{int(min_price * 3):,} تومان", ""),
    #             Button.url(f"{int(min_price * 4):,} تومان", ""),
    #         ],
    #         [
    #             Button.inline(InlineButtonsString.CUSTOM_CHARGE, "ONLINE-CUSTOM-CHARGE")
    #         ],
    #     ]
        
    #     return buttons

