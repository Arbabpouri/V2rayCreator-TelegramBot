from config import Config
from requests import post
from json import loads
from modules.requests_to_api.data_for_send import Data
from modules.requests_to_api.response_code import ResponseCode, ResponseResult


class ApiConfig:

    def __init__(self) -> None:
        pass


    @staticmethod
    async def get_token() -> None | bool:

        data = Data()
        req = post(url=Config.TOKEN, data=data.get_token)

        if (req.status_code != 200):
            del (data, req)
            return False
        
        result = loads(req.content)
        status_code = int(result["status_code"])

        if (status_code == ResponseCode.SUCSESS):
            result = result["result"]
            result_code = int(result["resultCode"])

            if (result_code):
                with open(r"./config/token.txt", "w+") as file:
                    file.write(str(result["jwtToken"]))
                del (data, result, status_code, result_code, file)
                return True

            else:
                print(
                    "Error : {}".format("Username is wrong" if (result_code == ResponseResult.USERNAME_ERROR) else \
                                        "Password is wrong" if (result_code == ResponseResult.PASSWORD_ERROR) else "Server Error")
                )
                exit()

        else:
            del (data, result, status_code)
            return False
