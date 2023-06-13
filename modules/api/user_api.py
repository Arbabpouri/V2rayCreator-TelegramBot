from requests import (
    post,
    put, 
    get
)
from json import loads
from typing import Optional, List
from modules.enums.enums import ResponseCode
from modules.models.api_response import (
    GetUserConfigsResult,
    GetUserInfoResult,
)
from modules.models import Models
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
        self.response = Models.get_response_from_api
        self.send_data = Models.send_data_to_api
        self.headers = self.send_data.Headers(Authorization=self.urls.TOKEN)


    @property
    def get_user_information(self) -> GetUserInfoResult | bool:
        """_summary_

        Args:
            user_id (int): _description_

        Returns:
            GetUserInfoResult | bool: _description_
        """

        for i in range(2):
            
            url = self.urls.get_user_info(self.user_id)
            response = get(
                url=url,
                headers=self.headers,
                verify=False
            )
            
            if (response.status_code == 200):

                result = self.response.GetUserInfo(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS): return result.result

                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):
                    
                    add_user = self.add_user()

                    if (not add_user): return False
                
                else: 
                    
                    return False

            elif (response.status_code == 401):

                ApiConfig().get_token
                continue

            else: 
                
                return False


    @property
    def get_user_type(self) -> int | bool:
        """
        for get user type , example : manual, seller and ...

        Returns:
            str | bool: _description_
        """

        data = self.send_data.UserId(userId=self.user_id).dict()

        for i in range(2):

            try:

                url = self.urls.get_user_type(self.user_id)
                response = get(
                    url=url, 
                    headers=self.headers,
                    verify=False
                )

                if (response.status_code == 200):

                    result = self.response.UserType(**loads(response.content))

                    if (result.status == ResponseCode.SUCSESS): 
                        return int(result.result.type)
                    
                    elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                        add_user = self.add_user()

                        if (not add_user): return False
                        continue

                    else: 
                        
                        return False
                
                elif (response.status_code == 401):
                    
                    ApiConfig().get_token
                    continue

                else:
                    
                    return False
                
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
                
                url = self.urls.get_user_configs(self.user_id)
                response = get(
                    url=url,
                    headers=self.headers,
                    verify=False
                )
                
                if (response.status_code == 200):

                    result = self.response.GetUserConfigs(**loads(response.content))
                    del response
                    
                    if (result.status == ResponseCode.SUCSESS):

                        return result.result

                    elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                        add_user = ApiConfig().get_token
                        
                        if (not add_user):
                            
                            return ResponseCode.FAILURE
                        
                    else:

                        return result.status  # 30, 32
                
                elif (response.status_code == 401):

                    count += 1
                    ApiConfig().get_token
                    continue

                else:

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
            
            url = self.urls.online_buy_config(
                user_id=int(self.user_id),
                server_id=int(server_id),
                config_type_id=int(config_id)
            )
            response = get(
                url=url,
                verify=False
            )
            
            if (response.status_code == 200):

                result = self.response.PaymentLink(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    return result.result
                
                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                    self.add_user()

                else:

                    return result.status  # 32, 42, 100, 102, 110

            elif (response.status_code == 401):

                ApiConfig().get_token

            else:

                return ResponseCode.FAILURE
        
        else:

            return ResponseCode.FAILURE


    def online_crypto_buy_link(self, server_id: int, config_id: int) -> str:

        """
        :param server_id:
        :param config_id:
        :return:
        """

        response = post(
            url=self.urls.online
        )


    def online_crypto_charge_link(self, amount: int) -> str:

        """
        :param amount:
        :return:
        """

        data = Data(self.user_id).cr


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

            url = self.urls.online_charge(
                user_id=int(self.user_id),
                amount=int(amount)
            )
            response = get(
                url=url,
                verify=False
            )
            
            if (response.status_code == 200):

                result = self.response.PaymentLink(**loads(response.content))
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
        
        data = self.send_data.AddNewUser(
            userId=int(self.user_id),
            referralerUserId=int(referraler)
        ).dict()

        for i in range(2):

            try:

                response = post(
                    url=self.urls.ADD_NEW_USER,
                    json=data,
                    headers=self.headers,
                    verify=False
                )
                
                if (response.status_code == 200):

                    result = self.response.AddUser(**loads(response.content))

                    if (result.status in [ResponseCode.SUCSESS, ResponseCode.USER_ALREADY_EXIST]):
                                                
                        return True
                    
                    return False
                
                elif (response.status_code == 401):

                    ApiConfig().get_token
                    continue

                else: 
                    
                    return False

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

            url = self.urls.increase_balance(self.user_id, how_much)
            response = put(
                url=url,
                headers=self.headers,
                verify=False
            )

            if (response.status_code == 200):

                result = self.response.IncreaseBalance(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    return True
                
                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                    user_api = self.add_user()
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
