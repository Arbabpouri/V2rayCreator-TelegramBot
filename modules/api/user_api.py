from requests import (
    post,
    put,
    get
)
from json import loads
from typing import Optional, List
from modules.enums.enums import ResponseCode, CryptoStatus
from modules.models.api_response import (
    GetUserConfigsResult,
    GetUserInfoResult,
    CryptoPayment
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
        self.headers = self.send_data.Headers(
            Authorization=self.urls.TOKEN
        ).dict()

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

                if (result.status == ResponseCode.SUCSESS):
                    return result.result

                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                    add_user = self.add_user()

                    if (not add_user):
                        return False

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

                        if (not add_user):
                            return False
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

        url = self.urls.get_user_configs(self.user_id)
        for i in range(2):

            try:

                response = get(
                    url=url,
                    headers=self.headers,
                    verify=False
                )

                if (response.status_code == 200):

                    result = self.response.GetUserConfigs(**loads(response.content))

                    if (result.status == ResponseCode.SUCSESS):

                        return result.result

                    elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                        add_user = ApiConfig().get_token

                        if (not add_user):

                            return ResponseCode.FAILURE

                    else:

                        return result.status  # 30, 32

                else:

                    return ResponseCode.FAILURE
                
            except Exception as error:
                print(error)
                continue

        return ResponseCode.FAILURE

    def online_crypto_buy_link(self, toman_amount: int, server_id: int, config_id: int) -> str:
        """
        :param server_id:
        :param config_id:
        :return:
        """

        data = self.send_data.CryptoOnlinePurchase(
            user_id=int(self.user_id),
            toman_amount=int(toman_amount),
            server_id=int(server_id),
            config_type_id=int(config_id),
        ).dict()

        for i in range(2):

            response = post(
                url=self.urls.CRYPTO_PAYMENT,
                data=data,
                verify=False
            )

            if (response.status_code == 200):

                result = self.response.CryptoPayment(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    return result

                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                    self.add_user()
                    continue

                else:

                    return ResponseCode.FAILURE
                
            else:

                return ResponseCode.FAILURE

        else:

            return ResponseCode.FAILURE

    def online_crypto_charge_link(self, toman_amount: int) -> CryptoPayment | int:
        """
        :param amount:
        :return:
        """

        data = self.send_data.CryptoCharge(
            user_id=int(self.user_id),
            toman_amount=int(toman_amount),
        ).dict()

        for i in range(2):

            response = post(
                url=self.urls.CRYPTO_PAYMENT,
                data=data,
                verify=False
            )

            if (response.status_code == 200):

                result = self.response.CryptoPayment(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    return result

                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                    self.add_user()
                    continue

                else:

                    return ResponseCode.FAILURE

            else:

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
        
        url = self.urls.online_charge(
                user_id=int(self.user_id),
                amount=int(amount)
            )

        for i in range(2):
            
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

                    return result.status  # 32, 40, 42

            elif (response.status_code == 401):

                ApiConfig().get_token

            else:

                return ResponseCode.FAILURE

        else:

            return ResponseCode.FAILURE

    def crypto_status(self, payment_id: int, crypto_payment_type: CryptoStatus, price: int) -> int:

        """_summary_

        Returns:
            _type_: _description_
        """

        data = self.send_data.CryptoGetStatus(price=price).dict()
        url = self.urls.crypto_check_status(
            crypto_payment_type=crypto_payment_type,
            payment_id=payment_id,
        )

        for i in range(2):

            response = get(
                url=url,
                data=data,
                verify=False
            )

            if (response.status_code == 200):

                result = self.response.CryptoPayment(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    return result.payment_status

                return result.status

            else:

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

        for i in range(2):

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
                    continue

                else:

                    return False

            elif (response.status_code == 401):

                ApiConfig().get_token
                continue

            else:

                return False

        else:

            return False
