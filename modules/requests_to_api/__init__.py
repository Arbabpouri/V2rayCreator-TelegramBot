from .bot import Database
from .v2ray import V2rayApi
from .api_config import ApiConfig


class APIS(Database, V2rayApi, ApiConfig):
    pass
