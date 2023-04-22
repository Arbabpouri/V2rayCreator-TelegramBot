from requests import post
from config import Config
from json import loads


class UserApi:

    # for add user to database
    async def add_user(self, user_id: int, referraler: int = 0) -> bool:
        if (not str(user_id).isnumeric() or not str(referraler).isnumeric()):
            raise ValueError("user_id or referraler argument is not a number")

        req = post(
            url=Config.ADD_USER_URL,
            data={
                "userId": int(user_id),
                "referralerUserId": int(referraler)
            }
        )
        result = loads(req.content)
        if (req.status_code == 200) and str(result["result"]) == "0":
            return True

        return False

    # for get user information(balance/configs/...)
    @staticmethod
    async def get_user_information(user_id) -> dict | bool:
        ...

    # for get user type , example : manual, seller and ...
    async def get_user_type(self, user_id: int) -> str | bool:
        if (not str(user_id).isnumeric()):
            raise ValueError("Invalid")

        req = post(
            url=Config.GET_USER_TYPE_URL,
            data={
                "userId": int(user_id),
            }
        )
        if (req.status_code == 200):
            result = loads(req.content)
            if (str(result["status"]) == "0"):
                del req
                return str(result["result"]["type"])

            #  TODO complet this session
            elif (str(result["status"]) == "1"):
                add_user = await self.add_user(user_id=user_id)
                if (add_user == 0):
                    del req
                    await self.get_user_type(user_id=user_id)

        return False
