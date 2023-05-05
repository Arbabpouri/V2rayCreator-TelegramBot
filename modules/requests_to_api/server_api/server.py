from typing import List, Dict
from requests import post
from json import loads
from config import Config
from modules.requests_to_api.json_to_object import GetAllConfigTypes
from modules.requests_to_api.data_for_send import Data
from modules.requests_to_api.response_code import ResponseCode



class V2Ray:

    def __init__(self) -> None:
        self.limit = 0


    @property
    def get_all_config_types(self) -> bool | List[Dict[str, str | int]]:
        '''
            request to api for get all config types
            return a list from the items in shop
        '''
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
            self.limit += 1

            if (self.limit == 0):
                
                del req
                self.get_all_config_types

            else:
                return False

        else:
            del req
            return False
