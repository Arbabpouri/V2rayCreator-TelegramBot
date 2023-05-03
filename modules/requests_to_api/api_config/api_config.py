from config import Config
from requests import post
from json import loads
from modules.requests_to_api.data_for_send import Data
from modules.requests_to_api.response_code import ResponseCode
from modules.requests_to_api.json_to_object import GetToken


class ApiConfig:

    def __init__(self) -> None:
        pass


    @property
    async def get_token() -> None | bool:

        data = Data()
        req = post(url=Config.TOKEN, data=data.get_token)

        if (req.status_code != 200):
            del (data, req)
            return False
        
        result = GetToken(**loads(req.content))

        if (result.status == ResponseCode.SUCSESS):

            with open(r"./config/token.txt", "w+") as file:
                file.write(result.result.jwtToken)
            del (data, result)
            return True

        else:
            print(
                "Error : {}".format("Username is wrong" if (result.status == ResponseCode.USERNAME_ERROR) else \
                                    "Password is wrong" if (result.status == ResponseCode.PASSWORD_ERROR) else result.message)
            )
            exit()

