from .bot import UserApi
from .v2ray import V2rayApi
from .api_config import ApiConfig


class APIS:
    UserApi = UserApi()
    V2rayApi = V2rayApi()
    ApiConfig = ApiConfig()
