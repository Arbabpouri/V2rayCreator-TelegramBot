from config import client
from modules.handlers import TextHandlers, InlineHandlers
from telethon.events import NewMessage, CallbackQuery
from modules.handlers.limiter import Limit
from modules.api.APIS import APIS
from modules.api.urls import ApiUrls


print('Imported')
if __name__ == "__main__":
    try:

        with open(r"./config/token.txt", "r") as file:
            ApiUrls().TOKEN = str(file.read())
            file.close()
        print("Token received")

        # for move user to different sessions
        client.add_event_handler(
            TextHandlers.user_move,
            NewMessage(
                func=lambda e: e.is_private and str(e.sender_id) not in list(Limit.LIMIT.keys())
            )
        )

        # for get information , example : get custom price for charge or etc
        client.add_event_handler(
            TextHandlers.get_informatios,
            NewMessage(
                func=lambda e: e.is_private and str(e.sender_id) in list(Limit.LIMIT.keys())
            )
        )

        # for set part
        client.add_event_handler(
            InlineHandlers.user_move,
            CallbackQuery(
                func=lambda e: e.is_private and str(e.sender_id) not in list(Limit.LIMIT.keys())
            )
        )

        print('Handlers Created\nBot is online')
        client.run_until_disconnected()

    except FileNotFoundError:

        APIS().config_api().get_token
        print("Please re run")
        exit()

    except Exception as ex:

        print(ex)
        exit()
