from telethon import Button
from . import TextButtunsString

class TextButtons:

    START_MENU = [
        [Button.text(TextButtunsString.BUY_CONFIG, resize= True, single_use= True)],
        [Button.text(TextButtunsString.MY_SUBSCRIPTIONS, resize= True, single_use= True), Button.text(TextButtunsString.ACCOUNT, resize= True, single_use= True)],
        [Button.text(TextButtunsString.GET_USER_ID, resize= True, single_use= True)],
        [Button.text(TextButtunsString.SHOP, resize= True, single_use= True), Button.text(TextButtunsString.REFRRAL, resize= True, single_use= True)],
        [Button.text(TextButtunsString.SUPPORT, resize= True, single_use= True)],
    ]

