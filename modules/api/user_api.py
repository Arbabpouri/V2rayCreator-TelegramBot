from requests import (post, put, delete, get)
from config import Config
from json import loads
from typing import Optional, List
from modules.api.data_for_send import Data
from modules.enums.enums import ResponseCode
from modules.models.api_response import (UserType,
                                        AddUser,
                                        GetUserConfigs,
                                        GetUserConfigsResult,
                                        GetUserInfo,
                                        GetUserInfoResult,
                                        PaymentLink)

from modules.api.api_config import ApiConfig
from modules.api.urls import ApiUrls




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


    @property
    def get_user_information(self) -> GetUserInfoResult | bool:
        """_summary_

        Args:
            user_id (int): _description_

        Returns:
            GetUserInfoResult | bool: _description_
        """

        for i in range(2):
            
            response = get(url=self.urls.get_user_info(int(self.user_id)),
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
                ApiConfig().get_token
                continue

            else:
                
                del response
                return False


    @property
    def get_user_type(self) -> int | bool:
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
                    return int(result.result.type)

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
                ApiConfig().get_token
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
        
        count = 0
        while (count < 2):
            
            response = get(url=self.urls.get_user_configs(self.user_id),
                             headers=self.headers)
            
            if (response.status_code == 200):

                result = GetUserConfigs(**loads(response.content))
                del response
                
                if (result.status == ResponseCode.SUCSESS):

                    return result.result

                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                    add_user = ApiConfig().get_token
                    
                    if (not add_user):
                        
                        del (add_user, result)
                        return False
                    
                else:

                    del response
                    return result.status  # 100, 32
            
            elif (response.status_code == 401):

                count += 1
                del response
                ApiConfig().get_token
                continue

            else:

                del response
                return False
    

    def online_buy_link(self, server_id: int, config_id: int) -> int | str:
        """_summary_

        Args:
            server_id (int): _description_
            config_id (int): _description_

        Returns:
            int | str: _description_
            int -> 32, 42, 100, 102, 110
            str -> link
        """

        for i in range(2):
            response = get(url=self.urls.online_buy_config(user_id=int(self.user_id),
                                                        server_id=int(server_id),
                                                        config_type_id=int(config_id)))
            
            if (response.status_code == 200):

                result = PaymentLink(**loads(response.content))
                del response

                if (result.status == ResponseCode.SUCSESS):

                    return result.result
                
                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                    self.add_user()

                else:

                    return result.status  # 32, 42, 100, 102, 110

            elif (response.status_code == 401):

                del response
                ApiConfig().get_token

            else:

                del response
                return ResponseCode.FAILURE
        
        else:

            return ResponseCode.FAILURE
    

    def online_charge_link(self, amount: int) -> int | str:
        """_summary_

        Args:
            amount (int): _description_

        Returns:
            int | str: _description_
            int -> 32, 40, 42
        """

        if (not str(amount).isnumeric()):
            raise ValueError("amount must be number")

        for i in range(2):
            response = get(url=self.urls.online_charge(user_id=int(self.user_id),
                                                       amount=int(amount)))
            
            if (response.status_code == 200):

                result = PaymentLink(**loads(response.content))
                del response

                if (result.status == ResponseCode.SUCSESS):

                    return result.result
                
                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                    self.add_user()

                else:

                    return result.status  # 32, 40, 42

            elif (response.status_code == 401):

                del response
                ApiConfig().get_token

            else:

                del response
                return ResponseCode.FAILURE
        
        else:

            return ResponseCode.FAILURE                


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
                ApiConfig().get_token
                continue

            else:
            
                del (data, response, result)
                return False
        
        else:

            del (data, response)
            return False
        

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
                ApiConfig().get_token

            else:

                del (data, response, count)
                return False
