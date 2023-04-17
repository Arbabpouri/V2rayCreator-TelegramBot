from telethon import Button
from . import UrlButtonsString, InlineButtonsData, InlineButtonsString
from config import Config
from modules.functions import create_payment_link


class UrlButtons:

    SUPPORT = [[Button.url(UrlButtonsString.SUPPORT, "https://t.me/{}".format(Config.ADMIN_USERNAME))]]

    @staticmethod
    def refrral(user_id: int) -> list:
        return [
            [
                Button.url(UrlButtonsString.REFRRAL, f"https://t.me/{Config.BOT_USERNAME}?start={user_id}")
            ],
        ]

    @staticmethod
    def shop(user_id: int, seller: bool) -> list:

        price = Config.USER_SHARJ if not seller else Config.SELLER_SHARJ

        buttons = []
        for i in range(0, len(price) - 1, 2):

            buttons.append(
                [
                    Button.url(UrlButtonsString.shop(price[i]), create_payment_link(user_id, price[i])),
                    Button.url(UrlButtonsString.shop(price[i + 1]), create_payment_link(user_id, price[i + 1]))
                ]
            )

        if len(price) % 2 != 0:

            buttons.append(
                [
                    Button.url(UrlButtonsString.shop(price[-1]), create_payment_link(user_id, price[-1]))
                ]
            )

        buttons.append(
            [
                Button.inline(InlineButtonsString.CUSTOM_SHARJ, InlineButtonsData.CUSTOM_SHARJ)
            ]
        )

        return buttons

    @staticmethod
    def payment_link(link) -> list:
        return [
            [
                Button.url(UrlButtonsString.CLICK_ME, link)
            ]
        ]
