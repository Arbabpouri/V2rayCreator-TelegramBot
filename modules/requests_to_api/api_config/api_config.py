from os import mkdir
from os.path import exists
from config import Config
from requests import post


class ApiConfig:

    @staticmethod
    async def get_token() -> None | bool:

        req = post(
            url=Config.TOKEN,
            data={
                "username": Config.USERNAME,
                "password": Config.PASSWORD,
            }
        )
        if (req.status_code == 200):
            ...

        return False


        # with open(r"./config/token.txt", "w+") as file:
        #     ...
