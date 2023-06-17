from telethon import Button
from typing import List, Optional, Tuple
from enum import StrEnum
from datetime import datetime

from modules.api.APIS import APIS
from modules.enums import UserTypes
from modules.models.api_response import GetAllConfigTypesResult
from modules.enums import ResponseCode
from config.bot_strings import Strings



class InlineButtonsString(StrEnum):
    BUY_CONFIG = ""
    CUSTOM_CHARGE = "💎 مبلغ دلخواه 💎"


class InlineButtons:

    def __init__(self, user_id: Optional[int] | None = None) -> None:
        self.user_id = user_id
        if (str(self.user_id).isnumeric()): self.user_api = APIS.user_api(int(user_id))
        self.v2ray = APIS.v2ray_api()
        self.CANCEL_GET = [Button.inline("❌ لغو عملیات ❌", "CANCEl-GET")]
        self.BACK_TO_HOME = [Button.inline("برگشت به خانه", "BACK-TO-HOME")]
        self.BACK_TO_CONFIGS = [Button.inline("⬅️ برگشت به لیست کانفیگ ها ⬅️", "BACK-TO-CONFIG-LIST")]

    @property
    def user_configs(self) -> Tuple[str, List[List[Button]]]:
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            Tuple[int: "Error code", List[List[Button]]]: _description_
            
        """
        

        if (not str(self.user_id).isnumeric()): raise ValueError("user_id must be number, example: InlineButtons(123456).user_configs()")

        configs = self.user_api.get_user_configs

        if (isinstance(configs, int)):

            message = Strings.RESPONSE_API_STRINGS[str(configs)] if (str(configs) in list(Strings.RESPONSE_API_STRINGS.keys()))\
                else Strings.ERROR
            return (message, self.BACK_TO_HOME)
        
        elif (not configs): 
            
            return (Strings.NOT_SERVICE, self.BACK_TO_HOME)

        buttons = [
            [
                Button.inline("نام سرور"),
                Button.inline("لوکیشن"),
                Button.inline("مدیریت"),
            ],
        ]

        for config in configs:
            
            buttons.append(
                [
                    Button.inline(str(config.name)),
                    Button.inline(str(config.serverName)),
                    Button.inline("مشاهده", f"SHOW-CONFIG-INFO-{config.id}"),
                ],
            )
        
        buttons.append(self.BACK_TO_HOME)
        
        return (Strings.SERVICES, buttons)

    def select_server(self, buy_or_change: Optional[str] = "BUY", config_id: int | str = "") -> Tuple[str, List[List[Button]]]:
        """_summary_

        Args:
            buy_or_change (Optional[str], optional): _description_. Defaults to "BUY".
            config_id (int | None, optional): _description_. Defaults to None.

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_

        Returns:
            Tuple[str, List[List[Button]]]: _description_
        """

        if (not str(self.user_id).isnumeric()): 
            raise ValueError("user_id must be integer")
        
        if (not isinstance(buy_or_change, str) or buy_or_change.upper() not in ["BUY", "CHANGE"]):
            raise ValueError("buy_or_change must be string and buy_or_change in ['BUY', 'CHANGE'].")
        
        if (buy_or_change.upper() == "CHANGE" and not str(config_id).isnumeric()):
            raise ValueError("whene time set CHANGE should gave number for config_id")

        servers = self.v2ray.get_all_servers
        user_type = self.user_api.get_user_type

        if (servers is False or
            not servers or
            user_type == UserTypes.MARKETER):

            buttons = [
                [Button.inline("❌ سروری برای نمایش وجود ندارد ❌")],
                self.BACK_TO_HOME
            ]

            return (Strings.NOT_SERVER, buttons)
        
        buttons = [
            [
                Button.inline("💢 نام سرور ")
            ]
        ]

        config = f"-{config_id}" if (buy_or_change.upper() == 'CHANGE') else ''
        for server in servers:
            buttons.append(
                [   
                    Button.inline(str(server.name), f"{buy_or_change.upper()}-SELECT-SERVER-{server.id}{config}"),
                ]
            )

        buttons.append(self.BACK_TO_HOME)

        return (Strings.BUY_CONFIG, buttons)

    def accept_admin_documents(self, name: str, user_name: str,
                               price: str, uuid: str) -> Tuple[bool, List[List[Button]]]:
        """_summary_

        Args:
            name (str): _description_
            user_name (str): _description_
            price (str): _description_
            uuid (str): _description_

        Raises:
            ValueError: _description_

        Returns:
            Tuple[bool, List[List[Button]]]: _description_
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

        Args:
            server_id (int): _description_

        Raises:
            ValueError: _description_

        Returns:
            Tuple[bool, List[List[Button]]]: _description_
        """
        
        if (not str(self.user_id).isnumeric() and
            not str(server_id).isnumeric()):

            raise ValueError("user/server id must be a number, example: InlineButtons(123456).configs_for_sell(12345)")

        configs = self.v2ray.get_all_config_types
        user_type = self.user_api.get_user_type
    
        if (configs is False or
            user_type == UserTypes.MARKETER):
            
            buttons = [
                [Button.inline("❌ کانفیگی برای نمایش وجود ندارد ❌")],
                [Button.inline("🔙 برگشت به لیست سرور ها", f"BACK-TO-SERVERS-{self.user_id}")]
            ]

            del (configs, user_type)
            return (False, buttons)
        
        buttons = [
            [
                Button.inline("💥نام"),
                Button.inline("💳 قیمت 'تومان'"),
            ]
        ]

        for config in configs:
            price = config.priceForManualUsers if (user_type == UserTypes.MANUAL) else config.priceForSellerUsers
            buttons.append(
                [
                    Button.inline(str(config.title), f"BUY-CONFIG-{server_id}-{config.id}"),
                    Button.inline(f"{int(price):,}"),
                ]
            )
        
        del (configs, user_type)
        return (True, buttons)

    def vmess_or_vless(self, server_id: int, config_id: int) -> List[List[Button]]:
        """_summary_

        Args:
            server_id (int): _description_
            config_id (int): _description_

        Raises:
            ValueError: _description_

        Returns:
            List[List[Button]]: _description_
        """

        if (not str(server_id).isnumeric() and
            not str(config_id).isnumeric()):

                raise ValueError("user/server/config id must be a number, example: InlineButtons(123456).vmess_or_vless(12345, 123)")
        
        return [
            [
                Button.inline("Vmess", f"BUY-SELECT-PROTOCOL-VMESS-{server_id}-{config_id}"),
                Button.inline("Vless", f"BUY-SELECT-PROTOCOL-VLESS-{server_id}-{config_id}"),
            ]
        ]

    def show_config(self, config_id: int) -> Tuple[str, List[List[Button]]]:

        if (not str(config_id).isnumeric()): raise ValueError("config_id must be integer")

        config_inform = self.v2ray.get_config(int(config_id))

        if (isinstance(config_inform, int)):
            
            message = Strings.RESPONSE_API_STRINGS[str(config_inform)] \
                if (str(config_inform) in Strings.RESPONSE_API_STRINGS.keys())\
                else Strings.ERROR
            
            return (message, self.BACK_TO_HOME)

        buttons = [
            [
                 Button.inline(f"⭕️ {config_inform.configTypeTitle} ⭕️"),  # title
            ],
            [
                Button.inline(f"👾 Name : {config_inform.name} 👾"),  # config name
            ],
            [
                Button.inline(f"🔌 Server Name: {config_inform.serverName} 🔌"),  # server name
            ],
            [
                Button.inline(f"🔩 Protocol: {config_inform.protocol} 🔩"),  # protocol
            ],
            [
                Button.inline(f"⚠️ Used: {config_inform.up + config_inform.down} ⚠️"),  # up + down
            ],
            [
                Button.inline(f"⬆️ Upload: {(config_inform.up) // (1024 ** 2)} ⬆️"),  # up
                Button.inline(f"⬇️ Download: {(config_inform.down) // (1024 ** 2)} ⬇️"),  # down
            ],
            [
                Button.inline(f"⏳ Remainde: {datetime.fromisoformat(config_inform.expiresDate) - datetime.now()}")  # zaman baghi munde
            ],
            [
                Button.inline(f"🛠 Construction: {config_inform.creationDate.replace('Z', '').replace('T', ' ')}"),  # zaman kharid
            ],
            [
                Button.inline(f"🪦 Expiration: {config_inform.expiresDate.replace('Z', '').replace('T', ' ')}"),  # zaman engheza
            ],
            [
                Button.inline("Status: " + "✅ فعال" if (config_inform.isEnable) else "❌ غیر فعال"),  # status
            ],
            [
                Button.inline("♻️ تمدید کانفیگ ♻️", f"RENEWAL-CONFIG-{config_id}")  # renewal config
            ],
            [
                Button.inline("🚩 تغییر سرور 🚩", f"CHANGE-SERVER-{config_id}"),  # change server
                Button.inline("⚙️ تغییر پروتوکل ⚙️", f"CHANGE-PROTOCOL-{config_id}"),  # change protocol
            ],
        ]

        buttons.append(self.BACK_TO_CONFIGS)

        return ("ok my bro", buttons)

    def acc_reject(self, amount: int) -> List[List[Button]]:
        """_summary_

        Args:
            amount (int): _description_

        Returns:
            List[List[Button]]: _description_
        """

        buttons = [
            [
                Button.inline("💳 درخواست جدید 💳"),
            ],
            [
                Button.inline("قبول کرد ✅", f"acc-{self.user_id}-{amount}"),
                Button.inline("رد کردن ❌", f"reject-{self.user_id}-{amount}"),
            ]
        ]

        return buttons
    
    def crypto_status(self, payment_id: int, crypto_amount: int, toman_amount: int) -> List[Button]:
        """_summary_

        Args:
            payment_id (int): _description_
            amount (int): _description_

        Returns:
            List[List[Button]]: _description_
        """

        buttons = [
            Button.inline("📍 با کریپتو پرداخت کردم 📍", f"CRYPTO-STATUS-{payment_id}-{crypto_amount}-{toman_amount}")
        ]

        return buttons

    def crypto_status_online(self, payment_id: int, amount: int, server_id: int, config_id: int) -> List[Button]:
        """_summary_

        Args:
            payment_id (int): _description_
            amount (int): _description_
            server_id (int): _description_
            config_id (int): _description_

        Returns:
            _type_: _description_
        """

        buttons = [
            Button.inline(
            text="🔹پرداخت با کریپتو | دریافت کانفیگ🔹", 
            data=f"CRYPTO-ONLINE-STATUS-{payment_id}-{amount}-{server_id}-{config_id}")
        ]

        return buttons

    def select_plan_online_buy(self, amount: int) -> List[List[Button]]:

        buttons = [
            [
                Button.inline("💳 خرید انلاین با ریال 💳", f"IRR-PAYMENT-{self.user_id}-{amount}")
            ],
            [
                Button.inline("💎 پرداخت انلاین با ارز دیجیتال 💎", f"CRYPTO-PAYMENT-{self.user_id}-{amount}")
            ]
        ]

        return buttons

