from telethon import Button
from typing import List, Optional, Dict
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
        price: str
    ) -> List[Button]:
        
        data = 0

        return [
            [Button.inline("💎 Name"), Button.inline(str(name))],
            [Button.inline("💎 User Name"), Button.inline(str(user_name))],
            [Button.inline("💎 User ID"), Button.inline(str(user_id))],
            [Button.inline("💎 Price"), Button.inline(f"{int(price):,} تومان")],
            [Button.inline("✅ تایید کردن", data["acc"]), Button.inline("❌ رد کردن", data["reject"])]
        ]
