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
            result_code = result["resultCode"]

            if (str(result["resultCode"]) == "ye"):  # Todo this session
                with open(r"./config/token.txt", "w+") as file:
                    file.write(str(result["jwtToken"]))
                return True

            else:
                print(
                    "Error : {}".format(
                        "Username is wrong" if (str(result["resultCode"]) == "0") else "Password is wrong" if 
                        (str(result["resultCode"]) == "1") else "Server Error"
                    )
                )
                exit()
        else:
            pass

        
