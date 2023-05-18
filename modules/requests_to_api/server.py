from typing import List, Dict, Optional
from requests import post
from json import loads
from config import Config
from modules.models.models import GetAllConfigTypes
from modules.requests_to_api.data_for_send import Data
from modules.enums.response_code import ResponseCode



class V2Ray:


    @property
    def get_all_config_types(self) -> bool | List[Dict[str, str | int]]:
        '''
            request to api for get all config types
            return a list from the items in shop
        '''
        i = 0
        while (i < 2):

            req = post(url=Config.GET_ALL_CONFIG_URL, headers=0)
            
            if (req.status_code == 200):

                result = GetAllConfigTypes(loads(req.content))

                if (result.status == ResponseCode.SUCSESS):

                    del req
                    return result.result.configTypes
                
                else:

                    del (req, result)
                    return False
                
            elif (req.status_code == 401):
               
                del req
                i += 1

            else:
                del req
                return False
            
        del req
        return False
        

    def create_config(self, user_id, admin: Optional[bool]=False):
        """
        
        """
        
        pass
    

    
