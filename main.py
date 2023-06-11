from telethon.events import NewMessage, CallbackQuery
from aiocron import crontab
from pystyle import Colors, Write

from config import client, Config
from modules.handlers import TextHandlers, InlineHandlers
from modules.handlers.limiter import Limit
from modules.api.APIS import APIS
from modules.api.urls import ApiUrls
from modules.tools.check_configs import check_config



Write.Print("Modules imported", Colors.red_to_green, end="\n")
if __name__ == "__main__":
    
    try:

        with open(r"./config/token.txt", "r") as file:

            ApiUrls.TOKEN = file.read()
            Write.Print("Token received", Colors.purple_to_blue, end="\n")
            file.close()
    
    except FileNotFoundError:

        APIS().config_api().get_token
        Write.Print("Please re run", Colors.red, end="\n")
        exit()

    except Exception as error:

        Write.Print(str(error), Colors.red, interval=0)
        exit()
        
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

    client.add_event_handler(
        InlineHandlers.acc_reject,
        CallbackQuery(
            func=lambda event: str(event.sender_id) not in list(Limit.LIMIT.keys()) \
                and event.sender_id in Config.ADMINS_USER_ID
        )
    )

    crontab(
        spec="* */6 * * *",
        func=check_config,
    )


    Write.Print('Handlers Created\nBot is online', Colors.blue_to_green, end="\n")
    client.run_until_disconnected()
