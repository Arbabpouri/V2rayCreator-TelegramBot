from config import client, config
from modules import user_move, refrral, inline_set_part, get_informatios
from telethon.events import NewMessage, CallbackQuery
from modules import Limit

print('Imported')
if __name__ == "__main__":
    try:

        client.add_event_handler(
            user_move,
            NewMessage(
                func= lambda e: e.is_private and str(e.sender_id) not in list(Limit.LIMIT.keys())
            )
        ) # for move user to difrrent sessions

        client.add_event_handler(
            get_informatios,
            NewMessage(
                func= lambda e: e.is_private and str(e.sender_id) in list(Limit.LIMIT.keys())
            )
        ) # for get informations , example : get custom price for sharj or etc

        client.add_event_handler(
            refrral,
            NewMessage(
                pattern=r"^/start [0-9]",
                func= lambda e: e.is_private and str(e.sender_id) not in list(Limit.LIMIT.keys())
            )
        ) # for refrrals

        client.add_event_handler(
            inline_set_part,
            CallbackQuery(
                func= lambda e: e.is_private and str(e.sender_id) not in list(Limit.LIMIT.keys())
            )
        ) # for set part


        print('Handlers Created\nBot is online')
        client.run_until_disconnected()


    except Exception as ex:

        print(ex)
