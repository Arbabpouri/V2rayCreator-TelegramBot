from telethon import Button
from modules.api.APIS import APIS
from typing import List
from enum import StrEnum
from modules.enums import UserTypes



class TextButtunsString(StrEnum):

    BUY_CONFIG = "⚡️ خرید سرویس ⚡️"
    MY_SUBSCRIPTIONS = "♻️ سرویس های من"
    ACCOUNT = "👤 حساب کاربری"
    REFERRAL = "🔗 زیرمجموعه گیری"
    SUPPORT = "☎️ پشتیبانی"
    SHOP = "💳 شارژ حساب"
    GET_USER_ID = "📍 شناسه کاربری"
    ONLINE_CHARGE = "🌐 شارژ آنلاین"
    OFFLINE_CHARGE = "💳 کارت به کارت"
    CRYPTO_CHARGE = "💎 پرداخت با ارز دیجیتال 💎"
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
            Button.text(TextButtunsString.CRYPTO_CHARGE, resize=True, single_use=True)
        ],
        [
            Button.text(TextButtunsString.BACK_TO_START_MENU, resize=True, single_use=True)
        ],
    ]


    @staticmethod
    def start_menu(user_id: int) -> List[List[Button]]:


        if (not str(user_id).isnumeric()):
            raise ValueError("user_id argument not a number")
        
        user_api = APIS.user_api(int(user_id))
        user_type = user_api.get_user_type

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
                Button.text(TextButtunsString.SUPPORT, resize=True, single_use=True),
                Button.text(TextButtunsString.GET_USER_ID, resize=True, single_use=True),
            ],
            [
                Button.text(TextButtunsString.REFERRAL, resize=True, single_use=True),
            ] if (user_type != UserTypes.SELLER) else [],

        ]

    

