from requests import (post, put, delete, get)
from config import Config
from json import loads
from typing import Optional, List
from modules.api.data_for_send import Data
from modules.enums.enums import ResponseCode
from modules.models.api_response import (
    UserType,
    AddUser,
    GetUserConfigs,
    GetUserConfigsResult,
    GetUserInfo,
    GetUserInfoResult,
    PaymentLink,
    IncreaseBalance
)

from modules.api.api_config import ApiConfig
from modules.api.urls import ApiUrls




class UserApi:

    def __init__(self, user_id: int) -> None:
        """_summary_

        Args:
            user_id (int): _description_

        Raises:
            ValueError: _description_
        """

        self.user_id = user_id
        self.urls = ApiUrls()
        self.headers = Data().headers

    @property
    def get_user_information(self) -> GetUserInfoResult | bool:
        """_summary_

        Args:
            user_id (int): _description_

        Returns:
            GetUserInfoResult | bool: _description_
        """

        for i in range(2):
            
            response = get(
                url=self.urls.get_user_info(self.user_id),
                headers=self.headers,
                verify=False
            )
            
            if (response.status_code == 200):

                result = GetUserInfo(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS): return result.result

                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):
                    
                    add_user = self.add_user()

                    if (not add_user): return False
                
                else: return False

            elif (response.status_code == 401):

                ApiConfig().get_token
                continue

            else: return False

    @property
    def get_user_type(self) -> int | bool:
        """
        for get user type , example : manual, seller and ...

        Returns:
            str | bool: _description_
        """

        data = Data(user_id=self.user_id)

        for i in range(2):

            try:

                response = get(
                    url=self.urls.get_user_type(self.user_id), 
                    headers=self.headers,
                    verify=False
                )

                if (response.status_code == 200):

                    result = UserType(**loads(response.content))

                    if (result.status == ResponseCode.SUCSESS): 
                        return int(result.result.type)
                    
                    elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                        add_user = self.add_user()

                        if (not add_user): return False
                        continue

                    else: return False
                
                elif (response.status_code == 401):
                    
                    ApiConfig().get_token
                    continue

                else: return False
                
            except Exception as error:

                print(error)
                continue

        
        return False

    @property
    def get_user_configs(self) -> List[GetUserConfigsResult] | int:
        """_summary_

        Returns:
            List[GetUserConfigsResult] | int: _description_
            int -> 30, 32
        """
        
        count = 0
        while (count < 2):

            try:
            
                response = get(
                    url=self.urls.get_user_configs(self.user_id),
                    headers=self.headers,
                    verify=False
                )
                
                if (response.status_code == 200):

                    result = GetUserConfigs(**loads(response.content))
                    del response
                    
                    if (result.status == ResponseCode.SUCSESS):

                        return result.result

                    elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                        add_user = ApiConfig().get_token
                        
                        if (not add_user):
                            
                            del (add_user, result)
                            return ResponseCode.FAILURE
                        
                    else:

                        del response
                        return result.status  # 30, 32
                
                elif (response.status_code == 401):

                    count += 1
                    del response
                    ApiConfig().get_token
                    continue

                else:

                    del response
                    return ResponseCode.FAILURE
            except Exception as error:
                print(error)
                count += 1
                continue

        return ResponseCode.FAILURE

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
            response = get(
                url=self.urls.online_buy_config(
                    user_id=int(self.user_id),
                    server_id=int(server_id),
                    config_type_id=int(config_id)
                ),
                verify=False
            )
            
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

    def online_crypto_buy_link(self, server_id: int, config_id: int) -> str:

        pass


    def online_crypto_charge_link(self, amount: int) -> str:

        pass


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
            response = get(
                url=self.urls.online_charge(
                    user_id=int(self.user_id),
                    amount=int(amount)
                ),
                verify=False
            )
            
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
        
        data = Data(
            user_id=self.user_id, 
            referraler=int(referraler)
        )

        for i in range(2):

            try:

                response = post(
                    url=self.urls.ADD_NEW_USER,
                    json=data.add_user,
                    headers=self.headers,
                    verify=False
                )
                
                if (response.status_code == 200):

                    result = AddUser(**loads(response.content))

                    if (result.status in [ResponseCode.SUCSESS, ResponseCode.USER_ALREADY_EXIST]):
                                                
                        return True
                    
                    return False
                
                elif (response.status_code == 401):

                    ApiConfig().get_token
                    continue

                else: return False

            except Exception as error:
                
                print(error)
                return False
        
        else:

            return False

    def balance_increase(self, how_much: int) -> bool:
        """
        for balance increase in database 

        Args:
            how_much (int): this argument for balance increase in database

        Returns:
            bool: successful or unsuccessful
        """

        if (not str(how_much).isnumeric()): raise ValueError("how_much must be an integer")
        
        count = 0
        while (count < 2):

            response = put(
                url=self.urls.increase_balance(self.user_id, how_much),
                headers=self.headers,
                verify=False
            )

            if (response.status_code == 200):

                result = IncreaseBalance(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):
                    return True
                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):
                    user_api = UserApi(self.user_id).add_user()
                    count += 1
                    continue
                else:
                    return False

            elif (response.status_code == 401):
                count += 1
                ApiConfig().get_token
                continue
            else:
                return False

        else:
            return False
