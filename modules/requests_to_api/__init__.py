from .bot import UserApi
from .server_api import V2Ray
from .api_config import ApiConfig
from typing import Optional


class APIS:
    def __init__(self) -> None:
        pass
    
    
    @staticmethod
    def user_api(user_id: int) -> UserApi:
        return UserApi(user_id=user_id)
    

    