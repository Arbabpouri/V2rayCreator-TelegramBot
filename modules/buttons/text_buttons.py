from telethon import Button
from modules.requests_to_api import APIS
from typing import List
from enum import StrEnum



class TextButtunsString(StrEnum):

    BUY_CONFIG = "⚡️ خرید سرویس ⚡️"
    MY_SUBSCRIPTIONS = "♻️ سرویس های من"
    ACCOUNT = "👤 حساب کاربری"
    REFERRAL = "🔗 زیرمجموعه گیری"
    SUPPORT = "☎️  پشتیبانی ☎️"
    SHOP = "🛒 فروشگاه"
    GET_USER_ID = "📍 شناسه کاربری 📍"


class TextButtons:

    @staticmethod
    def start_menu(user_id: int) -> List[Button]:

        if (not str(user_id).isnumeric()):
            raise ValueError("user_id argument not a number")

        return [
            [
                Button.text(TextButtunsString.BUY_CONFIG, resize=True, single_use=True),
            ],
            [
                Button.text(TextButtunsString.MY_SUBSCRIPTIONS, resize=True, single_use=True),
                Button.text(TextButtunsString.ACCOUNT, resize=True, single_use=True),
            ],
            [
                Button.text(TextButtunsString.SHOP, resize=True, single_use=True),
                Button.text(TextButtunsString.GET_USER_ID, resize=True, single_use=True),
            ],
            [
                Button.text(TextButtunsString.REFERRAL, resize=True, single_use=True),
            ] if (APIS.user_api(int(user_id)).get_user_type != 1) else [],
            [
                Button.text(TextButtunsString.SUPPORT, resize=True, single_use=True),
            ],
        ]
