from telethon import Button
from typing import List, Optional, Tuple
from enum import StrEnum
from modules.api.APIS import APIS
from modules.enums.types import UserTypes
from modules.models.api_response import GetAllConfigTypesResult



class InlineButtonsString(StrEnum):
    BUY_CONFIG = ""
    CUSTOM_CHARGE = "💎 مبلغ دلخواه 💎"


class InlineButtons:


    def __init__(self, user_id: Optional[int] | None = None) -> None:
        self.user_id = user_id
        self.v2ray = APIS.v2ray_api()
        self.CANCEL_GET = [Button.inline("❌ لغو عملیات ❌", "CANCEl-GET")]
        self.BACK_TO_HOME = [Button.inline("برگشت به خانه", "BACK-TO-HOME")]


    @property
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
        user_api = APIS.user_api(int(self.user_id))
        user_type = user_api.get_user_type

        if (servers is False or
            not servers or
            user_api == UserTypes.MARKETER):

            buttons = [
                [Button.inline("❌ سروری برای نمایش وجود ندارد ❌")],
                self.BACK_TO_HOME
            ]

            return (False, buttons)
        
        buttons = [
            [
                Button.inline("🔢 شماره"),
                Button.inline("💢 نام سرور ")
            ]
        ]

        for num, server in enumerate(servers):
            buttons.append(
                [   
                    Button.inline(str(num)), 
                    Button.inline(str(server.name), f"SELECT-SERVER-{server.id}")
                ]
            )

        del (servers, user_api, user_type)
        return (True, buttons)


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


    def configs_for_sell(self, server_id: int) -> Tuple[bool, List[List[Button]]]:
        """_summary_

        Returns:
            Tuple[bool, List[List[Button]]]: _description_
        """
        
        if (not str(self.user_id).isnumeric() and
            not str(server_id).isnumeric()):

            raise ValueError("user/server id must be a number, example: InlineButtons(123456).configs_for_sell(12345)")

        configs = self.v2ray.get_all_config_types
        user_api = APIS.user_api(int(self.user_id))
        user_type = user_api.get_user_type
    
        if (configs is False or
            user_type == UserTypes.MARKETER):
            
            buttons = [
                [Button.inline("❌ کانفیگی برای نمایش وجود ندارد ❌")],
                [Button.inline("🔙 برگشت به لیست سرور ها", f"BACK-TO-SERVERS-{self.user_id}")]
            ]

            del (configs, user_api, user_type)
            return (False, buttons)
        
        buttons = [
            [
                Button.inline("🔢 شماره"),
                Button.inline("💥نام"),
                Button.inline("📍کاربره"),
                Button.inline("💎حجم"),
                Button.inline("⌛مدت"),
                Button.inline("💳قیمت"),
                Button.inline("🔑خرید"),
            ]
        ]
        
        config: GetAllConfigTypesResult
        for config, num in enumerate(configs):
            price = config.priceForManualUsers if (user_type == UserTypes.MANUAL) else config.priceForSellerUsers
            buttons.append(
                [
                    Button.inline(str(num)),
                    Button.inline(str(config.title)),
                    Button.inline(f"{config.numberOfUsers} کاربره"),
                    Button.inline(f"{config.maxTraffic} گیگابایت"),
                    Button.inline(f"{config.activeTime} روزه"),
                    Button.inline(f"{int(price):,} تومان"),
                    Button.inline("خرید", f"BUY-CONFIG-{server_id}-{config.id}"),
                ]
            )
        
        del (configs, user_api, user_type)
        return (True, buttons)


    def vmess_or_vless(self, server_id: int, config_id: int) -> List[List[Button]]:
        """_summary_

        Args:
            server_id (int): _description_
            config_id (int): _description_
            price (int): _description_

        Returns:
            List[List[Button]]: _description_
        """

        if (not str(self.user_id).isnumeric() and
            not str(server_id).isnumeric() and
            not str(config_id).isnumeric()):

                raise ValueError("user/server/config id must be a number, example: InlineButtons(123456).vmess_or_vless(12345, 123)")
        
        return [
            [
                Button.inline("Vmess", f"BUY-SELECT-PROTOCOL-VMESS-{server_id}-{config_id}"),
                Button.inline("Vless", f"BUY-SELECT-PROTOCOL-VLESS-{server_id}-{config_id}"),
            ]
        ]
