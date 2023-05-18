from requests import post
from config import Config
from json import loads
from typing import Optional
from modules.requests_to_api.data_for_send import Data
from modules.requests_to_api.response_code import ResponseCode
from modules.models.models import UserType, AddUser
from modules.requests_to_api import APIS




class UserApi:


    def __new__(cls, user_id):
        """_summary_

        Args:
            user_id (_type_): _description_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """

        if (not str(user_id).isnumeric()):
            raise ValueError("User id must be numeric")
        return super().__new__(cls, user_id)


    def __init__(self, user_id: int) -> None:
        """_summary_

        Args:
            user_id (int): _description_

        Raises:
            ValueError: _description_
        """

        self.user_id = int(user_id)


    def add_user(self, referraler: Optional[int] = 0) -> bool:
        """
        for add user to database

        Args:
            referraler (Optional[int], optional): _description_. Defaults to 0.

        Raises:
            ValueError: _description_

        Returns:
            bool | ValueError: _description_
        """
        
        if (not str(referraler).isnumeric()):
            raise ValueError("referraler argument is not a number")
        
        data = Data(user_id=self.user_id, referraler=int(referraler))
        for i in range(2):

            responsive = post(url=Config.ADD_USER_URL, data=data.add_user)
            
            if (responsive.status_code == 200):
                result = AddUser(**loads(responsive.content))

                if (result.status in [ResponseCode.SUCSESS, ResponseCode.USER_ALREADY_EXISTS]):
                    del (data, responsive, result)
                    return True
                
                del (data, responsive, result)
                return False
            
            elif (responsive.status_code == 401):

                del responsive
                APIS.config_api().get_token

            else:
            
                del (data, responsive, result)
                return False
        
        else:
            del (data, responsive)
            return False

    # TODO : this function 
    def balance_increase(self, price: int) -> bool:
        """
        for balance increase in database 

        Args:
            price (int): this argument for balance increase in database

        Returns:
            bool: successful or unsuccessful
        """

        if (not str(price).isnumeric()): raise ValueError("price must be an integer")
        
        data = Data(self.user_id).balance_increase(int(price))
        count = 0
        while (count < 2):

            responsive = post(url=Config.BALANCE_INCREASE, data="", headers=Config.TOKEN)
            if (responsive.status_code == 200):

                result = loads(responsive.content)
                if ():

                    pass

                else:

                    pass
                
            elif (responsive.status_code == 401):
                
                del responsive
                count += 1
                APIS.config_api().get_token

            else:

                del (data, responsive, count)
                return False

    @property
    def get_user_information(self) -> int | bool:
        """
            for get user information(balance/configs/...)
        """


    @property
    def get_user_type(self) -> str | bool:
        """
        for get user type , example : manual, seller and ...

        Returns:
            str | bool: _description_
        """

        data = Data(user_id=self.user_id)
        count = 0
        while (count < 2):

            responsive = post(url=Config.GET_USER_TYPE_URL, data=data.userId)

            if (responsive.status_code == 200):

                result = UserType(**loads(responsive.content))

                if (result.status == ResponseCode.SUCSESS):
                    del (responsive, data)
                    return str(result.result.type)

                elif (result.status == ResponseCode.USER_NOT_FOUND):
                    add_user = self.add_user()

                    if (add_user):
                        del (responsive, data, add_user, result)
                        continue
                    else:
                        del (responsive, add_user, result)
                        count += 1
                        continue

                else:
                    del (responsive, data, result)
                    return False
            
            elif (responsive.status_code == 401):
                
                del responsive
                count += 1
                APIS.config_api().get_token

            else:

                del (data, responsive)
                return False
        
        del (responsive, data)
        return False
