from typing import Optional

from modules.enums.enums import CryptoPaymentType


class ApiUrls:

    TOKEN: str = ""

    def __init__(self) -> None:

        self.API_URL = "https://cnmellat.top/api"
        self.CRYPTO_API_URL = "https://mellatking.top/api"
        # this is url for get token for request to api
        self.GET_TOKEN = fr"{self.API_URL}/Auth/LogIn"
        # this is url for add user
        self.ADD_NEW_USER = fr"{self.API_URL}/Users/AddNewUser"
        # this is url for get all config
        self.GET_ALL_CONFIG_TYPES = fr"{self.API_URL}/ConfigTypes/GetAllConfigTypes"
        self.ADD_NEW_CONFIG = fr"{self.API_URL}/Configs/AddNewConfig"  #
        self.GET_ALL_SERVERS = fr"{self.API_URL}/Servers/GetAllServers"  #
        self.GET_SETTINGS = fr"{self.API_URL}/Settings/GetSettings"  #
        self.RENEWAL_CONFIG = fr"{self.API_URL}/Configs/RenewalConfig"  #
        self.CHANGE_SERVER = fr"{self.API_URL}/Configs/ChangeServer"
        self.CRYPTO_PAYMENT = fr"{self.CRYPTO_API_URL}/payment"

    def get_user_type(self, user_id) -> str:
        """_summary_

        Args:
            user_id (_type_): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}/Users/GetUserType?userId={user_id}"

    def get_user_info(self, user_id) -> str:
        """_summary_

        Args:
            user_id (_type_): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}/Users/GetUserInfo?userId={user_id}"

    def get_config_with_id(self, config_id) -> str:
        """_summary_

        Args:
            config_id (_type_): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}/Configs/GetConfig?configId={config_id}"

    def get_user_configs(self, user_id) -> str:
        """_summary_

        Args:
            user_id (_type_): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}/Configs/GetUserConfigs?userId={user_id}"

    def change_protocol(self, config_id) -> str:
        """_summary_

        Args:
            config_id (_type_): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}/Configs/ChangeProtocol?configId={config_id}"

    def delete_config(self, config_id) -> str:
        """_summary_

        Args:
            config_id (_type_): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}/Configs/DeleteConfig?configId={config_id}"

    def online_buy_config(
        self,
        user_id: int,
        server_id: int,
        config_type_id: int
    ) -> str:
        """_summary_
        """

        return fr"{self.API_URL}/Gateway/GenOnlinePurchaseGateway?UserId={user_id}&ServerId={server_id}&ConfigTypeId={config_type_id}"

    def online_charge(self, user_id: int, amount: int) -> str:
        """_summary_

        Args:
            user_id (int): _description_
            amount (float): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}/Gateway/GenChargeGateway?UserId={user_id}&Amount={amount}"

    def get_all_configs(self, server_id: int) -> str:

        return fr"{self.API_URL}/Configs/GetAllConfigs?ServerId={server_id}"

    def increase_balance(self, user_id: int, how_much: int) -> str:
        """
        :param user_id: int
        :param how_much: int
        :return: str
        """

        return fr"{self.API_URL}/Users/ChangeUserMoney?userId={user_id}&howMuch={how_much}"

    def crypto_check_status(self, crypto_payment_type: int, payment_id: int) -> str:

        return fr"{self.CRYPTO_API_URL}/payment/status?payment_id={payment_id}&crypto_payment_type={crypto_payment_type}"

    def crypto_payment_url(self, amount: int, address: str, currency: Optional[str] = "TRX") -> str:
        """_summary_

        Args:
            amount (int): _description_
            address (str): _description_
            currency (Optional[str], optional): _description_. Defaults to "TRX".

        Returns:
            str: _description_
        """
        
        return fr"https://weswap.digital/quick/?amount={amount}&currency={currency}&address={address}"
