from config import client, config
from modules import user_move, referral_handler, inline_set_part, get_informatios
from telethon.events import NewMessage, CallbackQuery
from modules import Limit

print('Imported')
if __name__ == "__main__":
    try:

        # for move user to different sessions
        client.add_event_handler(
            user_move,
            NewMessage(
                func=lambda e: e.is_private and str(e.sender_id) not in list(Limit.LIMIT.keys())
            )
        )
        # for get information , example : get custom price for charge or etc
        client.add_event_handler(
            get_informatios,
            NewMessage(
                func=lambda e: e.is_private and str(e.sender_id) in list(Limit.LIMIT.keys())
            )
        )
        # for referrals
        client.add_event_handler(
            referral_handler,
            NewMessage(
                pattern=r"^/start [0-9]",
                func=lambda e: e.is_private and str(e.sender_id) not in list(Limit.LIMIT.keys())
            )
        )
        # for set part
        client.add_event_handler(
            inline_set_part,
            CallbackQuery(
                func=lambda e: e.is_private and str(e.sender_id) not in list(Limit.LIMIT.keys())
            )
        )

        print('Handlers Created\nBot is online')
        client.run_until_disconnected()

    except Exception as ex:

        print(ex)
