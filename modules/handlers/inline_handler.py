from config import client, Strings
from modules.buttons import InlineButtonsData
from modules.handlers.limiter import Limit, Step
from telethon.events import CallbackQuery



async def inline_set_part(event: CallbackQuery.Event) -> None:

    data = bytes(event.data).decode()
    match(data):

        case (InlineButtonsData.CUSTOM_CHARGE):

            await client.send_message(
                event.chat_id,
                Strings.GET_CUSTOM_SHARJ
            )

            Limit.LIMIT[str(event.sender_id)] = {
                "part": Step.GET_CUSTOM_SHARJ
            }

        case _:
            pass
