from requests import post
from config import Config
from json import loads
from typing import Optional
from modules.requests_to_api.bot.data import Data



class UserApi:

    def __init__(self, user_id: int) -> None:
        
        if (not str(user_id).isnumeric()):
            raise ValueError("User id must be numeric")
        self.user_id = int(user_id)


    def add_user(self, referraler: Optional[int] = 0) -> bool | ValueError:
        '''
            for add user to database
        '''
        if (not str(referraler).isnumeric()):
            raise ValueError("referraler argument is not a number")
        
        data = Data(user_id=self.user_id, referraler=int(referraler))
        req = post(url=Config.ADD_USER_URL, data=data.add_user)
        result = loads(req.content)
        if (req.status_code == 200) and str(result["result"]) == "0":
            del (data, referraler, req, result)
            return True

        return False


    def get_user_information(self) -> dict | bool | ValueError:
        '''
            for get user information(balance/configs/...)
        '''


    def get_user_type(self) -> str | bool | ValueError: 
        ''''
            for get user type , example : manual, seller and ...
        '''
        if (not str(self.user_id).isnumeric()):
            raise ValueError("user_id must be integer")
        
        data = Data(user_id=self.user_id)
        req = post(url=Config.GET_USER_TYPE_URL, data=data.userId)
        if (req.status_code == 200):
            result = loads(req.content)
            result_code = str(result["status"])
            if (result_code == "0"):
                del (req, data, result_code)
                return str(result["result"]["type"])

            #  TODO complet this session
            elif (result_code == "1"):
                add_user = self.add_user(user_id=self.user_id)
                if (add_user):
                    del (req, data, add_user, result_code)
                    self.get_user_type(user_id=self.user_id)

        return False
