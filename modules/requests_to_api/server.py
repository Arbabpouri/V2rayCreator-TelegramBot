from typing import List, Dict, Optional
from requests import (post, get, put, delete)
from json import loads
from modules.models.api_respons import (GetAllConfigTypes,
                                        GetAllConfigTypesResult,
                                        AddNewConfig,
                                        AddNewConfigResult,
                                        ChangeProtocol, ChangeProtocolResult,
                                        ChangeServer,
                                        ChangeServerResult)

from modules.requests_to_api.data_for_send import Data
from modules.enums.response_code import ResponseCode
from modules.requests_to_api.urls import ApiUrls



class V2Ray:


    def __init__(self) -> None:
        self.Urls = ApiUrls()


    @property
    def get_all_config_types(self) -> bool | List[GetAllConfigTypesResult]:
        '''
            responsiveuest to api for get all config types
            return a list from the items in shop
        '''
        i = 0
        while (i < 2):

            responsive = post(url=self.Urls.GET_ALL_CONFIG_TYPES, headers=0)
            
            if (responsive.status_code == 200):

                result = GetAllConfigTypes(loads(responsive.content))

                if (result.status == ResponseCode.SUCSESS):

                    del responsive
                    return result.result.configTypes
                
                else:

                    del (responsive, result)
                    return False
                
            elif (responsive.status_code == 401):
               
                del responsive
                i += 1

            else:
                del responsive
                return False
            
        del responsive
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
            
            responsive = post(url=self.Urls.ADD_NEW_CONFIG,
                              data=data,
                              headers=Data.headers)
            
            if (responsive.status_code == 200):

                result = AddNewConfig(**loads(responsive.content))

                if (result.status == ResponseCode.SUCSESS):
                    
                    pass

                elif (result.status == ResponseCode.USER_DOES_NOT_EXIST):

                    pass



            elif (responsive.status_code == 401):

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

            responsive = get(url=self.Urls.get_config_with_id(config_id),
                             headers=Data.headers)
            
            if (responsive.status_code == 200):

                result = GetAllConfigTypes(**loads(responsive.content))
                if (result.status == ResponseCode.SUCSESS):

                    pass

                elif (result.status == ResponseCode.CONFIG_DOES_NOT_EXIST):

                    pass

                else:

                    pass

            elif (responsive.status_code == 401):

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

        i = 0
        while (i < 2):

            responsive = put(url=self.Urls.change_protocol(int(config_id)),
                             headers=Data.headers)
            
            if (responsive.status_code == 200):

                result = ChangeProtocol(**loads(responsive.content))

                if (result.status == ResponseCode.SUCSESS):

                    pass

                else:

                    del responsive
                    return result.status

            elif (responsive.status_code == 401):

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
        
        i = 0
        while (i < 2):
            data = Data().change_server(int(config_id), int(target_server_id))
            responsive = put(url=self.Urls.CHANGE_SERVER,
                             data=data,
                             headers=Data.headers)
            
            if (responsive.status_code == 200):

                result = ChangeServer(**loads(responsive.content))

                if (result.status == ResponseCode.SUCSESS):

                    pass

                else:

                    del responsive
                    return result.status

            elif (responsive.status_code == 401):
                
                pass

            else:

                pass










