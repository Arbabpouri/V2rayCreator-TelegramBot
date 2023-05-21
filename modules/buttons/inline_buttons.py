from telethon import Button
from typing import List
from enum import StrEnum



class InlineButtonsString(StrEnum):
    BUY_CONFIG = ""
    CUSTOM_CHARGE = "💎 مبلغ دلخواه 💎"
    CANCEL_GET = "❌ لغو عملیات ❌"



class InlineButtons:
    CANCEL_GET = [[Button.inline(InlineButtonsString.CANCEL_GET, "CANCEl-GET")]]


    @staticmethod
    def accept_admin_documents(
        name: str,
        user_id: str,
        user_name: str,
        price: str,
        uuid: str
    ) -> List[Button]:
        
        return [
            [Button.inline("💎 Name"), Button.inline(str(name))],
            [Button.inline("💎 User Name"), Button.inline(str(user_name))],
            [Button.inline("💎 User ID"), Button.inline(str(user_id))],
            [Button.inline("💎 Price"), Button.inline(f"{int(price):,} تومان")],
            [Button.inline("✅ تایید کردن", f"acc-{uuid}"), Button.inline("❌ رد کردن", f"reject-{uuid}")]
        ]
