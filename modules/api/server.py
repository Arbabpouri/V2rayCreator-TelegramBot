from typing import List, Optional
from requests import (
    post,
    get,
    put,
    delete
)
from json import loads
from itertools import chain
from modules.models.api_response import (
    GetAllConfigTypesResult,
    AddNewConfigResult,
    ChangeProtocolResult,
    ChangeServerResult,
    RenewalConfigResult,
    GetAllServerResult,
    GetConfigResult,
    GetAllConfigsResult
)
from modules.models import Models
from modules.enums import ResponseCode
from modules.api.urls import ApiUrls
from modules.api.api_config import ApiConfig
from modules.api.user_api import UserApi
from modules.api.api_config import ApiConfig


class V2Ray:

    def __init__(self) -> None:

        self.urls = ApiUrls()
        self.response = Models.get_response_from_api
        self.send_data = Models.send_data_to_api
        self.headers = self.send_data.Headers(
            Authorization=self.urls.TOKEN).dict()

    @property
    def get_all_config_types(self) -> List[GetAllConfigTypesResult] | int:
        """_summary_

        Returns:
            List[GetAllConfigTypesResult]: _description_
            int: 1 -> Failur
        """

        i = 0
        while (i < 2):

            try:

                response = get(
                    url=self.urls.GET_ALL_CONFIG_TYPES,
                    headers=self.headers,
                    verify=False
                )

                if (response.status_code == 200):

                    result = self.response.GetAllConfigTypes(
                        **loads(response.content))

                    if (result.status == ResponseCode.SUCSESS):

                        return result.result.configTypes

                    return ResponseCode.FAILURE

                elif (response.status_code == 401):

                    ApiConfig().get_token
                    continue

                else:

                    return ResponseCode.FAILURE

            except Exception as error:

                print(error)
                i += 1
                continue

        return []

    @property
    def get_all_servers(self) -> List[GetAllServerResult] | bool:

        for i in range(2):

            response = get(
                url=self.urls.GET_ALL_SERVERS,
                headers=self.headers,
                verify=False
            )

            if (response.status_code == 200):

                result = self.response.GetAllServer(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    return result.result.servers

                return False

            elif (response.status_code == 401):

                ApiConfig().get_token
                continue

            else:

                return False

        else:

            return False

    @property
    def get_all_configs(self) -> List[GetAllConfigsResult] | bool | list:
        """_summary_

        Returns:
            List[GetAllConfigsResult] | bool | list: _description_
        """

        servers = self.get_all_servers
        if (not servers):
            return False
        

        for server in servers:
            configs: list = []

            response = get(
                url=self.urls.get_all_configs(server.id),
                headers=self.headers,
                verify=False
            )

            if (response.status_code == 200):

                result = self.response.GetAllConfigs(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):
                    
                    configs: list = [result.result]
                    configs = chain.from_iterable(configs)

            elif (response.status_code == 401):

                ApiConfig().get_token
                continue

        return configs

    def add_new_config(
        self,
        user_id: int,
        server_id: int,
        config_type_id: int,
        protocol: str,
        is_free: Optional[bool] = False
    ) -> AddNewConfigResult | int:
        """_summary_

        Args:
            user_id (int): _description_
            server_id (int): _description_
            config_type_id (int): _description_
            protocol (str): _description_
            is_free (Optional[bool], optional): _description_. Defaults to False.

        Returns:
            AddNewConfigResult | int: _description_
            int - > 32, 110, 100, 41, 102, 130
        """

        data = self.send_data.AddNewConfig(
            userId=int(user_id),
            serverId=int(server_id),
            configTypeId=int(config_type_id),
            protocol=str(protocol),
            isFree=bool(is_free)
        ).dict()

        for i in range(2):

            response = post(
                url=self.urls.ADD_NEW_CONFIG,
                json=data,
                headers=self.headers,
                verify=False
            )

            if (response.status_code == 200):

                result = self.response.AddNewConfig(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    return result.result

                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                    add_user = UserApi(int(user_id)).add_user()

                    if (not add_user):

                        return ResponseCode.FAILURE

                else:

                    return result.status  # 32, 110, 100, 41, 102, 130

            elif (response.status_code == 401):

                ApiConfig().get_token
                continue

            else:

                return False

    def get_config(self, config_id: int) -> GetConfigResult | int:
        """_summary_

        Args:
            config_id (int): _description_

        Returns:
            GetConfigResult: _description_
            int: 120 -> config does not exist , 1 -> Failur
        """

        for i in range(2):

            response = get(
                url=self.urls.get_config_with_id(config_id),
                headers=self.headers,
                verify=False
            )

            if (response.status_code == 200):

                result = self.response.GetConfig(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    return result.result

                return result.status  # 120

            elif (response.status_code == 401):

                ApiConfig().get_token
                continue

            else:

                return ResponseCode.FAILURE

    def change_protocol(self, config_id: int) -> ChangeProtocolResult | int:
        """_summary_

        Args:
            config_id (int): _description_

        Returns:
            ChangeProtocolResult: _description_
        """

        for i in range(2):

            response = put(
                url=self.urls.change_protocol(int(config_id)),
                headers=self.headers,
                verify=False
            )

            if (response.status_code == 200):

                result = self.response.ChangeProtocol(
                    **loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    return result.result

                return result.status  # 120, 121, 130

            elif (response.status_code == 401):

                ApiConfig().get_token
                continue

            else:

                return ResponseCode.FAILURE

    def change_server(self, config_id: int, target_server_id: int) -> ChangeServerResult | int:
        """_summary_

        Args:
            config_id (int): _description_
            target_server_id (int): _description_

        Returns:
            ChangeServerResult | int: _description_
        """

        data = self.send_data.ChangeServer(
            configId=int(config_id),
            targeterverId=int(target_server_id)
        ).dict()

        for i in range(2):

            response = put(
                url=self.urls.CHANGE_SERVER,
                json=data,
                headers=self.headers,
                verify=False
            )

            if (response.status_code == 200):

                result = self.response.ChangeServer(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    return result.result

                return result.status  # 100, 102, 120, 121, 130

            elif (response.status_code == 401):

                ApiConfig().get_token
                continue

            else:

                return ResponseCode.FAILURE

    def renewal_config(self, config_id: int) -> RenewalConfigResult | int | bool:
        """_summary_

        Args:
            config_id (int): _description_

        Returns:
            RenewalConfigResult | int: _description_
        """

        data = self.send_data.RenewalConfig(configId=int(config_id)).dict()

        for i in range(2):

            response = put(
                url=self.urls.RENEWAL_CONFIG,
                json=data,
                headers=self.headers,
                verify=False
            )

            if (response.status_code == 200):

                result = self.response.RenewalConfig(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    return result.result

                return result.status  # 41, 120, 122, 131

            elif (response.status_code == 401):

                ApiConfig().get_token
                continue

            else:

                return ResponseCode.FAILURE

    def delete_config(self, config_id: int) -> bool | int:
        """_summary_

        Args:
            config_id (int): _description_

        Returns:
            DeleteConfig | int: _description_
        """

        for i in range(2):

            response = delete(
                url=self.urls.delete_config(int(config_id)),
                headers=self.headers,
                verify=False
            )

            if (response.status_code == 200):

                result = self.response.DeleteConfig(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    return True

                return result.status  # 120, 132

            elif (response.status_code == 401):

                ApiConfig().get_token
                continue

            else:

                return False
