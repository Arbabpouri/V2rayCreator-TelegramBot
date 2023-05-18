class Config:

    API_ID = 3359959  # Telegram Api ID , you can get it from telegram website
    API_HASH = "fc809b5d42bdac477f9ac9b56383a699"  # Telegram Api Hash , you can get it from telegram website
    BOT_TOKEN = "5867054982:AAH6SDlVaeULkaw5WF2aJSe3TiCvvMK5qq8"   # Bot Token,you can get it from @BotFather
    ADMIN_USERNAME = ""  # Admin Username without @ , example: SirSardar . ** for supporter **
    ADMINS_USER_ID = []  # Admins user id for send deposit documents 
    BOT_USERNAME = "V2rayCreatorBot"  # without the @ , example : V2rayCreatorBot
    SESSION_NAME = "bot"  # string
    USER_CHARGE = [50000, 100000, 150000, 200000]  # T
    SELLER_CHARGE = [500000, 1000000, 1500000, 2000000]  # T
    MIN_USER_CHARGE = 25000  # T , for min charge by manual user
    MIN_SELLER_CHARGE = 500000  # T , for min charge by seller user
    CARD_NUMBER = "1234 5678 9876 5432"
    CARD_HOLDER = "علی مومنی"

    # API Config
    PAYMENT_DOMAIN = "127.0.0.1"  # payment url for buy
    API_URL = "0.0.0.0"  # this is url for requesting
    TOKEN = "" # jwt token for send in header
    USERNAME = ""  # username for login to api for get token
    PASSWORD = ""  # password for login to api for get token
    GET_TOKEN = r"{}/api/Auth/LogIn".format(API_URL)  # this is url for get token for request to api
    GET_USER_TYPE = r"{}/api/Users/GetUserType".format(API_URL)   # this is url for get user
    ADD_NEW_USER = r"{}/api/Users/AddNewUser".format(API_URL)  # this is url for add user
    GET_ALL_CONFIG_TYPES = r"{}/api/ConfigTypes/GetAllConfigTypes".format(API_URL)  # this is url for get all config
    GET_USER_TYPE = r"{}/api/Users/GetUserType".format(API_URL)  # this is url for get user type
    GET_USER_INFO = r"{}/api/Users/GetUserInfo".format(API_URL)
    BALANCE_INCREASE = r"{}/".format(API_URL)  # this is url for balance increase TODO
    GET_CONFIG_WITH_ID = r"{}/api/Configs/GetConfig".format(API_URL)
    GET_USER_CONFIGS = r"{}api/Configs/GetUserConfigs".format(API_URL)
    ADD_NEW_CONFIG = r"{}/api/Configs/AddNewConfig".format(API_URL)
    CHANGE_PROTOCOL = r"{}/api/Configs/ChangeProtocol".format(API_URL)
    CHANGE_SERVER = r"{}/api/Configs/ChangeServer".format(API_URL)
    RENEWAL_CONFIG = r"{}/api/Configs/RenewalConfig".format(API_URL)
    DELETE_CONFIG = r"{}/api/Configs/DeleteConfig".format(API_URL)
    GET_ALL_SERVERS = r"{}/api/Servers/GetAllServers".format(API_URL)
    GET_SETTINGS = r"{}/api/Settings/GetSettings".format(API_URL)



def __check_config() -> bool:
    pass