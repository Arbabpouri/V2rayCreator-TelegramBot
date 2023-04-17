from telethon import Button
from . import TextButtunsString
from modules.requests_to_api import APIS


class TextButtons:

    def start_menu(UserId: int) -> list | ValueError:
        if not str(UserId).isnumeric():
            raise ValueError("User id argument not a number")

        return [
            [
                Button.text(TextButtunsString.BUY_CONFIG, resize= True, single_use= True),
            ],
            [
                Button.text(TextButtunsString.MY_SUBSCRIPTIONS, resize= True, single_use= True),
                Button.text(TextButtunsString.ACCOUNT, resize= True, single_use= True),
            ],
            [
                Button.text(TextButtunsString.SHOP, resize= True, single_use= True),
                Button.text(TextButtunsString.GET_USER_ID, resize=True, single_use=True),
            ],
            [
                Button.text(TextButtunsString.REFRRAL, resize= True, single_use= True),
            ] if not APIS.is_seller(int(UserId)) else [],
            [
                Button.text(TextButtunsString.SUPPORT, resize= True, single_use= True),
            ],
        ]

