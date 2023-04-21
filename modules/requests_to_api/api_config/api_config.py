from os import mkdir
from os.path import exists
from config import Config
from requests import post
from json import loads


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
        result = loads(req.content)
        if (req.status_code == 200 and str(req["status_code"]) == "0"):
            del req
            
            
            

        return False


        # with open(r"./config/token.txt", "w+") as file:
        #     ...
