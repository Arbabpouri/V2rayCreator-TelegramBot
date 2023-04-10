from telethon import Button
from . import UrlButtonsString, InlineButtonsData, InlineButtonsString
from config import Config
from modules.functions import create_payment_link
class UrlButtons:
    refrral = lambda UserId: [[Button.url(UrlButtonsString.REFRRAL, f"https://t.me/{Config.BOT_USERNAME}?start={UserId}")]]
    SUPPORT = [[Button.url(UrlButtonsString.SUPPORT, "https://t.me/{}".format(Config.ADMIN_USERNAME))]]

    def shop(UserID: int, Seller: bool) -> list:

        Price = Config.USER_SHARJ if Seller == False else Config.SELLER_SHARJ

        buttons = []
        for i in range(0, len(Price) - 1, 2):

            buttons.append(
                [
                    Button.url(UrlButtonsString.SHOP(Price[i]), create_payment_link(UserID, Price[i])),
                    Button.url(UrlButtonsString.SHOP(Price[i + 1]), create_payment_link(UserID, Price[i + 1]))
                ]
            )

        if len(Price) % 2 != 0:

            buttons.append(
                [
                    Button.url(UrlButtonsString.SHOP(Price[-1]), create_payment_link(UserID, Price[-1]))
                ]
            )

        buttons.append(
            [
                Button.inline(InlineButtonsString.CUSTOM_SHARJ, InlineButtonsData.CUSTOM_SHARJ)
            ]
        )

        return  buttons


    def payment_link(link) -> list:
        return [
            [
                Button.url(UrlButtonsString.CLICK_ME, link)
            ]
        ]