from config import Config
from requests import post
from json import loads
from modules.requests_to_api.api_config.data import Data


class ApiConfig:

    def __init__(self) -> None:
        pass


    @staticmethod
    async def get_token() -> None | bool:

        data = Data()
        req = post(
            url=Config.TOKEN,
            data=data.get_token
        )

        if (req.status_code != 200):
            del (data, req)
            return False
        
        result = loads(req.content)
        status_code = int(result["status_code"])

        if (status_code == 0):
            result = result["result"]
            result_code = int(result["resultCode"])

            if (result_code == 0):  # Todo this session
                with open(r"./config/token.txt", "w+") as file:
                    file.write(str(result["jwtToken"]))
                del (data, result, status_code, result_code)
                return True

            else:
                print(
                    "Error : {}".format(
                        "Username is wrong" if (result_code == 1) else "Password is wrong" if 
                        (result_code == 2) else "Server Error"
                    )
                )
                exit()

        del (data, result, status_code)
        return False
