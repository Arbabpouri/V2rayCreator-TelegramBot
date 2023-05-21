from telethon import Button
from modules.api.APIS import APIS
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
    ONLINE_CHARGE = "🌐 شارژ آنلاین"
    OFFLINE_CHARGE = "💳 کارت به کارت"
    BACK_TO_START_MENU = "🔙 منوی اصلی 🔙"
    CANCEl_GET = "❌ لغو عملیات ❌"


class TextButtons:

    CANCEL_GET = [Button.text(TextButtunsString.CANCEl_GET, resize=True, single_use=True)]

    SELECT_CHARGE = [
            [
                Button.text(TextButtunsString.ONLINE_CHARGE, resize=True, single_use=True),
                Button.text(TextButtunsString.OFFLINE_CHARGE, resize=True, single_use=True)
            ],
            [
                Button.text(TextButtunsString.BACK_TO_START_MENU, resize=True, single_use=True)
            ]
        ]       


    @staticmethod
    def start_menu(user_id: int) -> List[Button]:
        """
        
        """

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

    

