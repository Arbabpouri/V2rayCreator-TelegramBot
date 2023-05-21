class ApiUrls:

    TOKEN: str = ""


    def __init__(self) -> None:
        self.API_URL = "http://cnmellat.top"
        self.GET_TOKEN = fr"{self.API_URL}/api/Auth/LogIn"  # this is url for get token for request to api
        self.ADD_NEW_USER = fr"{self.API_URL}/api/Users/AddNewUser"  # this is url for add user
        self.GET_ALL_CONFIG_TYPES = fr"{self.API_URL}/api/ConfigTypes/GetAllConfigTypes"  # this is url for get all config
        self.BALANCE_INCREASE = fr"{self.API_URL}/api/Users/"  # this is url for balance increase TODO
        self.ADD_NEW_CONFIG = fr"{self.API_URL}/api/Configs/AddNewConfig"  # 
        self.GET_ALL_SERVERS = fr"{self.API_URL}/api/Servers/GetAllServers"  # 
        self.GET_SETTINGS = fr"{self.API_URL}/api/Settings/GetSettings"  #
        self.HANGE_SERVER = fr"{self.API_URL}/api/Configs/ChangeServer"  # 
        self.RENEWAL_CONFIG = fr"{self.API_URL}/api/Configs/RenewalConfig"  # 
        self.CHANGE_SERVER = fr"{self.API_URL}/api/Configs/ChangeServer"  #
    
    
    def get_user_type(self, user_id) -> str:
        """_summary_

        Args:
            user_id (_type_): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}/api/Users/GetUserType?userId={user_id}"
    

    def get_user_info(self, user_id) -> str:
        """_summary_

        Args:
            user_id (_type_): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}/api/Users/GetUserInfo?userId={user_id}"


    def get_config_with_id(self, config_id) -> str:
        """_summary_

        Args:
            config_id (_type_): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}/api/Configs/GetConfig?configId={id}"
    

    def get_user_configs(self, user_id) -> str:
        """_summary_

        Args:
            user_id (_type_): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}api/Configs/GetUserConfigs?userId={user_id}"
    

    def change_protocol(self, config_id) -> str:
        """_summary_

        Args:
            config_id (_type_): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}/api/Configs/ChangeProtocol?configId={config_id}"
    

    def delete_config(self, config_id) -> str:
        """_summary_

        Args:
            config_id (_type_): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}/api/Configs/DeleteConfig?configId={config_id}"


    def online_buy_config(self, user_id: int, server_id: int,
                          config_type_id: int) -> str:
        
        """_summary_
        """

        return fr"{self.API_URL}/api/Gateway/GenOnlinePurchaseGateway"
    

    def online_charge(self, user_id: int, amount: float) -> str:
        """_summary_

        Args:
            user_id (int): _description_
            amount (float): _description_

        Returns:
            str: _description_
        """

        return fr"{self.API_URL}/api/Gateway/GenChargeGateway"



