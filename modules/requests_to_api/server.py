from typing import List, Dict, Optional
from requests import (post, get, put, delete)
from json import loads
from modules.models.api_respons import GetAllConfigTypes
from modules.requests_to_api.data_for_send import Data
from modules.enums.response_code import ResponseCode
from modules.requests_to_api.urls import ApiUrls



class V2Ray:


    def __init__(self) -> None:
        self.Urls = ApiUrls()


    @property
    def get_all_config_types(self) -> bool | List[Dict[str, str | int]]:
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
        

    def create_config(self, user_id, admin: Optional[bool]=False):
        """
        
        """
        
        pass
    

    def get_config(self, config_id):
        
        for i in range(2):
            responsive = ...
