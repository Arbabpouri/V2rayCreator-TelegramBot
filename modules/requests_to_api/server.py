from typing import List, Dict, Optional
from requests import (post, get, put, delete)
from json import loads
from modules.models.api_response import (GetAllConfigTypes,
                                        GetAllConfigTypesResult,
                                        AddNewConfig,
                                        AddNewConfigResult,
                                        ChangeProtocol, ChangeProtocolResult,
                                        ChangeServer,
                                        ChangeServerResult,
                                        RenewalConfig,
                                        RenewalConfigResult,
                                        DeleteConfig,
                                        )

from modules.requests_to_api.data_for_send import Data
from modules.enums.response_code import ResponseCode
from modules.requests_to_api.urls import ApiUrls



class V2Ray:


    def __init__(self) -> None:
        self.urls = ApiUrls()
        self.headers = self.headers


    @property
    def get_all_config_types(self) -> bool | List[GetAllConfigTypesResult]:
        '''
            responseuest to api for get all config types
            return a list from the items in shop
        '''
        i = 0
        while (i < 2):

            response = post(url=self.urls.GET_ALL_CONFIG_TYPES,
                            headers=self.headers)
            
            if (response.status_code == 200):

                result = GetAllConfigTypes(loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    del response
                    return result.result.configTypes
                
                else:

                    del (response, result)
                    return False
                
            elif (response.status_code == 401):
               
                del response
                i += 1

            else:
                del response
                return False
            
        del response
        return False
        

    def add_new_config(self, user_id, server_id, config_type_id, protocol, 
                       is_free: Optional[bool]=False) -> AddNewConfigResult | bool:
        """
        
        """
        
        for i in range(2):
            data = Data(user_id=int(user_id)).add_new_config(server_id=int(server_id),
                                                             config_type_id=int(config_type_id),
                                                             protocol=str(protocol),
                                                             is_free=bool(is_free))
            
            response = post(url=self.urls.ADD_NEW_CONFIG,
                              data=data,
                              headers=self.headers)
            
            if (response.status_code == 200):

                result = AddNewConfig(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):
                    
                    pass

                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                    pass



            elif (response.status_code == 401):

                pass

            else:

                pass
    

    def get_config(self, config_id: int) -> List[GetAllConfigTypesResult]:
        """_summary_

        Args:
            config_id (int): _description_

        Returns:
            List[GetAllConfigTypesResult]: _description_
        """
        
        for i in range(2):

            response = get(url=self.urls.get_config_with_id(config_id),
                             headers=self.headers)
            
            if (response.status_code == 200):

                result = GetAllConfigTypes(**loads(response.content))
                if (result.status == ResponseCode.SUCSESS):

                    pass

                elif (result.status == ResponseCode.CONFIG_DOES_NOT_EXIST):

                    pass

                else:

                    pass

            elif (response.status_code == 401):

                pass

            else:

                pass


    def chenge_protocol(self, config_id: int) -> ChangeProtocolResult | int:
        """_summary_

        Args:
            config_id (int): _description_

        Returns:
            ChangeProtocolResult: _description_
        """

        for i in range(2):

            response = put(url=self.urls.change_protocol(int(config_id)),
                             headers=self.headers)
            
            if (response.status_code == 200):

                result = ChangeProtocol(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    pass

                del response
                return result.status

            elif (response.status_code == 401):

                pass

            else:

                pass


    def change_server(self, config_id: int, target_server_id: int) -> ChangeServerResult | int:
        """_summary_

        Args:
            config_id (int): _description_
            target_server_id (int): _description_

        Returns:
            ChangeServerResult | int: _description_
        """
        
        for i in range(2):

            data = Data().change_server(int(config_id), int(target_server_id))
            response = put(url=self.urls.CHANGE_SERVER,
                             data=data,
                             headers=self.headers)
            
            if (response.status_code == 200):

                result = ChangeServer(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    pass

                del response
                return result.status  # 120

            elif (response.status_code == 401):
                
                pass

            else:

                pass


    def renewal_config(self, config_id: int) -> RenewalConfigResult | int:
        """_summary_

        Args:
            config_id (int): _description_

        Returns:
            RenewalConfigResult | int: _description_
        """

        for i in range(2):
            
            data = Data().config_id(int(config_id))
            response = put(url=self.urls.RENEWAL_CONFIG,
                          data=data,
                          headers=self.headers)
            
            if (response.status_code == 200):

                result = RenewalConfig(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    pass
         
                del response
                return result.status  # 41, 120, 122, 131

            elif (response.status_code == 401):

                pass

            else:

                pass


    def delete_config(self, config_id: int) -> DeleteConfig | int:
        """_summary_

        Args:
            config_id (int): _description_

        Returns:
            DeleteConfig | int: _description_
        """

        for i in range(2):

            response = delete(url=self.urls.delete_config(int(config_id)),
                              headers=self.headers)
            
            if (response.status_code == 200):

                result = DeleteConfig(**loads(response.content))

                if (result.status == ResponseCode.SUCSESS):

                    pass
                
                del response
                return result.status  # 120, 132

            elif (response.status_code == 401):
                
                pass

            else:

                pass


    @property
    def get_all_servers(self):

        for i in range(2):

            response = get(url=self.urls.GET_ALL_SERVERS,
                           headers=self.headers)
            
            if (response.status_code == 200):

                result = ...

            elif (response.status_code == 401):

                pass

            else:

                pass

                