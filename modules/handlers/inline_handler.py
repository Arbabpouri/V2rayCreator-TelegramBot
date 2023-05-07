from config import client, Strings
from modules import InlineButtonsData, TextButtons
from modules.handlers.limiter import Limit, Step
from telethon.events import CallbackQuery


class InlineHandlers:

    @staticmethod
    async def inline_set_part(event: CallbackQuery.Event) -> None:

        data = bytes(event.data).decode()
        match(data):

            case ("CUSTOM-CHARGE"):

                await client.send_message(
                    event.chat_id,
                    Strings.GET_CUSTOM_CHARGE,
                    buttons=TextButtons.CANCEL_GET
                )

                Limit.LIMIT[str(event.sender_id)] = {"part": Step.GET_CUSTOM_CHARGE_ONLINE}

            case _:
                pass
    

    