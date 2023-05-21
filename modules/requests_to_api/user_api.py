from requests import (post, put, delete, get)
from config import Config
from json import loads
from typing import Optional, List
from modules.requests_to_api.data_for_send import Data
from modules.enums.response_code import ResponseCode
from modules.models.api_response import (UserType,
                                        AddUser,
                                        GetUserConfigs,
                                        GetUserConfigsResult,
                                        GetUserInfo,
                                        GetUserInfoResult)
from modules.requests_to_api import APIS
from modules.requests_to_api.urls import ApiUrls




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
        self.urls = ApiUrls()
        self.headers = self.headers


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

            response = post(url=self.urls.ADD_NEW_USER,
                            data=data.add_user,
                            headers=self.headers)
            
            if (response.status_code == 200):
                result = AddUser(**loads(response.content))
                del (data, response)

                if (result.status in [ResponseCode.SUCSESS, ResponseCode.USER_ALREADY_EXIST]):
                    
                    return True
                
                return False
            
            elif (response.status_code == 401):

                del response
                APIS().config_api().get_token
                continue

            else:
            
                del (data, response, result)
                return False
        
        else:

            del (data, response)
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

            response = post(url=self.urls.BALANCE_INCREASE,
                            data="",
                            headers=self.headers)
            if (response.status_code == 200):

                result = loads(response.content)
                if ():

                    pass

                else:

                    pass
                
            elif (response.status_code == 401):
                
                del response
                count += 1
                APIS.config_api().get_token

            else:

                del (data, response, count)
                return False


    def get_user_information(self, user_id: int) -> GetUserInfoResult | bool:
        """_summary_

        Args:
            user_id (int): _description_

        Returns:
            GetUserInfoResult | bool: _description_
        """

        for i in range(2):
            
            response = get(url=self.urls.get_user_info(int(user_id)),
                           headers=self.headers)
            
            if (response.status_code == 200):

                result = GetUserInfo(**loads(response.content))
                del response

                if (result.status == ResponseCode.SUCSESS):

                    return result.result

                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):
                    
                    add_user = self.add_user()

                    if (not add_user):

                        del add_user
                        return False
                
                else:

                    return False

            elif (response.status_code == 401):

                del response
                APIS().config_api().get_token
                continue

            else:
                
                del response
                return False

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

            response = post(url=self.urls.get_user_type(self.user_id), data=data.userId)

            if (response.status_code == 200):

                result = UserType(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):
                    del (response, data)
                    return str(result.result.type)

                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                    add_user = self.add_user()

                    if (not add_user):
                        del (response, add_user, result, data)
                        return False
                    
                    continue

                else:

                    del (response, data, result)
                    return False
            
            elif (response.status_code == 401):
                
                del response
                count += 1
                APIS.config_api().get_token
                continue

            else:

                del (data, response)
                return False
        
        del (response, data)
        return False

    
    @property
    def get_user_configs(self) -> List[GetUserConfigsResult] | bool | int:
        """_summary_

        Returns:
            List[GetUserConfigsResult]: _description_
        """
        
        i = 0
        while (i < 2):
            
            response = get(url=self.urls.get_user_configs(self.user_id),
                             headers=self.headers)
            
            if (response.status_code == 200):

                result = GetUserConfigs(**loads(response.content))
                del response
                
                if (result.status == ResponseCode.SUCSESS):

                    return result.result

                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                    add_user = APIS().config_api().get_token
                    
                    if (not add_user):
                        
                        del (add_user, result)
                        return False
                    
                else:

                    del response
                    return result.status  # 100, 32
            
            elif (response.status_code == 401):

                i += 1
                del response
                APIS().config_api().get_token
                continue

            else:

                del response
                return False
    
