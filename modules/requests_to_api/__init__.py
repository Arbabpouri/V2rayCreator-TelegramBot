from .bot import UserApi
from .server_api import V2Ray
from .api_config import ApiConfig



class APIS:
    
    @staticmethod
    def user_api(user_id: int) -> UserApi:
        return UserApi(user_id=user_id)
    

    @staticmethod
    def v2ray_api() -> V2Ray:
        return V2Ray()
    

    @staticmethod
    def config_api() -> ApiConfig:
        return ApiConfig()
    

    