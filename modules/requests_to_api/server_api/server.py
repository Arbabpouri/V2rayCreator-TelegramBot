from typing import List, Dict
from requests import post
from config import Config
from modules.requests_to_api.json_to_object import GetAllConfigTypes
from modules.requests_to_api.data_for_send import Data


Limiter = set({})

class V2Ray:
    
    def __init__(self) -> None:
        pass


    @property
    def get_all_config_types(self) -> bool | List[Dict[str, str | int]]:
        req = post(url=Config.GET_ALL_CONFIG_URL, headers=0)
        
        if (req.status_code == 200):
            pass

        elif (req.status_code == 401):
            if ():
                pass
            else:
                pass

        else:
            del req
            return False
        