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
        if (req.status_code == 200):
            result = loads(req.content)

            if (str(result["status_code"]) == "0"):
                result = result["result"]

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

        return False
