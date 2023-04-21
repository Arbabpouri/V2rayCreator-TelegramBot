from requests import post
from config import Config


class UserApi:

    def __init__(self) -> None:
        self.type_response = {
            "0": "manual",
            "1": "seller",
            "2": "marketer",
            "3": "nothing",
        }

    # for add user to database
    @staticmethod
    async def add_user(user_id: int, referraler: int = 0) -> bool:

        req = post(
            url=Config.ADD_USER_URL,
            data={
                "userId": user_id,
                "referralerUserId": referraler
            }
        )

        if (req.status_code == 200):

            result = req.json()
            if (str(result["result"]) == "0"):

                ...

            elif (str(result["result"]) == "1"):

                ...

            else:

                ...

        else:

            raise ConnectionError("Error in send request to API")

    # for get user type , example : manual, seller and ...
    async def get_user_type(self, user_id: int) -> str:

        if (not str(user_id).isnumeric()):

            raise ValueError("Invalid")

        req = post(
            url=Config.GET_USER_TYPE_URL,
            data={
                "userId": int(user_id),
            }
        )

        if (req.status_code != 200):

            result = req.json()
            del req
            if (str(result["status"]) == "0"):

                user_type = result["result"]["type"]
                del result
                return self.type_response[str(user_type)]

            elif (str(result["status"]) == "1"):

                ...

            else:

                # TODO: handle this session error
                ...

        else:

            raise ConnectionError("Error in send request to API")
