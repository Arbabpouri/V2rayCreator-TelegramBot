from modules.requests_to_api.user_api import UserApi
from modules.requests_to_api.server import V2Ray
from modules.requests_to_api.api_config import ApiConfig


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
    