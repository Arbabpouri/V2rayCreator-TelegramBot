from datetime import datetime
from telethon.types import PeerUser
from asyncio import sleep
from typing import NoReturn

from modules.api.APIS import APIS
from config import client
from config.bot_strings import Strings


async def check_config() -> NoReturn:

    v2ray = APIS.v2ray_api()
    configs = v2ray.get_all_configs

    if (not configs):
        return

    users = []

    for config in configs:

        time_remaining = (datetime.fromisoformat(config.expiresDate) - datetime.now()).days
        print(time_remaining)

        if (0 <= time_remaining <= 1):
            users.append(
                (config.clientUserId, config.v2RayLink)
            )

    for user, v2ray_link in users:

        try:

            await client.send_message(
                PeerUser(int(user)),
                Strings.end_config(user, v2ray_link),
            )
            await sleep(0.3)

        except:
            pass
