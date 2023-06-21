from telethon import Button
from typing import List, Optional
from config import Config


class UrlButtonsString:

    SUPPORT = "📞 ارتباط با ادمین 📞"
    REFERRAL = "💢 لینک زیر مجموعه گیری 💢"
    CLICK_ME = "📍 کلیک کنید 📍"
    CRYPTO_PAYMENT = "💎 پرداخت با ارز دیجیتال 💎"
    IRR_PAYMENT = "💳 پرداخت با ریال 💳"

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
    def payment_link(link: str, text: Optional[str] = UrlButtonsString.CLICK_ME) -> List[Button]:

        """
            
        """

        return [Button.url(text, link)]
