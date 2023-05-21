from telethon import Button
from typing import List, Optional, Tuple
from enum import StrEnum
from modules.api.APIS import APIS



class InlineButtonsString(StrEnum):
    BUY_CONFIG = ""
    CUSTOM_CHARGE = "💎 مبلغ دلخواه 💎"


class InlineButtons:
    CANCEL_GET = [[Button.inline("❌ لغو عملیات ❌", "CANCEl-GET")]]

    def __init__(self, user_id: Optional[int] | None = None) -> None:
        self.user_id = user_id
        self.v2ray = APIS.v2ray_api()


    def accept_admin_documents(self, name: str, user_name: str,
                               price: str, uuid: str) -> Tuple[bool, List[List[Button]]]:
        """_summary_

        Args:
            name (str): _description_
            user_id (str): _description_
            user_name (str): _description_
            price (str): _description_
            uuid (str): _description_

        Returns:
            List[List[Button]]: _description_
        """

        if (not str(self.user_id).isnumeric()):
            raise ValueError("user_id must be integer")

        return [
            [Button.inline("💎 Name"), Button.inline(str(name))],
            [Button.inline("💎 User Name"), Button.inline(str(user_name))],
            [Button.inline("💎 User ID"), Button.inline(str(self.user_id))],
            [Button.inline("💎 Price"), Button.inline(f"{int(price):,} تومان")],
            [Button.inline("✅ تایید کردن", f"ACC-{uuid}"), Button.inline("❌ رد کردن", f"REJECT-{uuid}")]
        ]


    def select_server(self) -> Tuple[bool, List[List[Button]]]:
        """_summary_

        Args:
            user_id (int): _description_

        Returns:
            List[List[Button]]: _description_
        """

        if (not str(self.user_id).isnumeric()):
            raise ValueError("user_id must be integer")

        servers = self.v2ray.get_all_servers

        if (servers is False or not servers):
            buttons = [
                [Button.inline("❌ سروری برای نمایش وجود ندارد ❌")],
                [Button.inline("🔙 برگشت به منوی اصلی", "BACK-TO-HOME")]
            ]

            return (False, buttons)
        
        buttons = [
            [Button.inline("🔢 تعداد"), Button.inline("💢 نام سرور ")]
        ]

        for num, server in enumerate(servers):
            buttons.append(
                [   
                    Button.inline(str(num)), 
                    Button.inline(str(server.name), f"SERVER-{self.user_id}-{server.id}")
                ]
            )

        del (servers)
        return (True, buttons)

    # TODO
    def configs_for_sell(self) -> Tuple[bool, List[List[Button]]]:
        """_summary_

        Returns:
            Tuple[bool, List[List[Button]]]: _description_
        """
        
        configs = self.v2ray.get_all_config_types
        
        if (configs is False):
            
            buttons = [
                [Button.inline("❌ کانفیگی برای نمایش وجود ندارد ❌")]
            ]
            return (False, buttons)
        
        buttons = [
            []
        ]

        for config, num in enumerate(configs):
            
            buttons.append(
                [

                ]
            )
        
        return (True, buttons)


