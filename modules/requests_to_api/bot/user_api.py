from requests import post
from config import Config
from json import loads
from typing import Optional
from modules.requests_to_api.data_for_send import Data
from modules.requests_to_api.response_code import ResponseCode
from modules.requests_to_api.json_to_object import UserType, AddUser



class UserApi:

    def __init__(self, user_id: int) -> None:
        
        if (not str(user_id).isnumeric()):
            raise ValueError("User id must be numeric")
        self.user_id = int(user_id)


    def add_user(self, referraler: Optional[int] = 0) -> bool | ValueError:
        '''
            for add user to database
            referraler must be integer
        '''
        
        if (not str(referraler).isnumeric()):
            raise ValueError("referraler argument is not a number")
        
        data = Data(user_id=self.user_id, referraler=int(referraler))
        req = post(url=Config.ADD_USER_URL, data=data.add_user)
        
        if (req.status_code != 200):
            ...

        result = AddUser(**loads(req.content))

        if str(result.status) == ResponseCode.SUCSESS:
            del (data, req, result)
            return True
        
        del (data, req, result)
        return False


    @property
    def get_user_information(self) -> dict | bool | ValueError:
        '''
            for get user information(balance/configs/...)
        '''


    @property
    def get_user_type(self) -> str | bool | ValueError:
        '''
            for get user type , example : manual, seller and ...
        '''
        
        data = Data(user_id=self.user_id)
        req = post(url=Config.GET_USER_TYPE_URL, data=data.userId)

        if (req.status_code != 200):
            del (data, req)
            return False
        
        result = UserType(**loads(req.content))

        if (result.status == ResponseCode.SUCSESS):
            del (req, data)
            return str(result.result.type)

        elif (result.status == ResponseCode.USER_NOT_FOUND):
            add_user = self.add_user(user_id=self.user_id)
            if (add_user):
                del (req, data, add_user)
                self.get_user_type
            else:
                return False

        else:
            return False
