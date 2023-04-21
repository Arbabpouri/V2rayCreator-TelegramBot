class Config:

    API_ID = 3359959  # Telegram Api ID , you can get it from telegram website
    API_HASH = "fc809b5d42bdac477f9ac9b56383a699"  # Telegram Api Hash , you can get it from telegram website
    BOT_TOKEN = "5867054982:AAH6SDlVaeULkaw5WF2aJSe3TiCvvMK5qq8"   # Bot Token,you can get it from @BotFather
    BOT_USERNAME = "V2rayCreatorBot"  # without the @ , example : V2rayCreatorBot
    SESSION_NAME = "bot"  # string
    USER_CHARGE = [50000, 100000, 150000, 200000]  # T
    SELLER_CHARGE = [500000, 1000000, 1500000, 2000000]  # T
    MIN_USER_CHARGE = 25000  # T , for min charge by manual user
    MIN_SELLER_CHARGE = 500000  # T , for min charge by seller user

    # API Config
    PAYMENT_DOMAIN = "127.0.0.1"  # payment url for buy
    API_URL = "0.0.0.0"  # this is url for requesting
    TOKEN = ""
    USERNAME = ""  # username for login to api for get token
    PASSWORD = ""  # password for login to api for get token
    GET_TOKEN_URL = r"{}/".format(API_URL)  # this is url for get token for request to api
    GET_USER_URL = r"{}/".format(API_URL)   # this is url for get user
    ADD_USER_URL = r"{}/".format(API_URL)  # this is url for add user
    GET_ALL_CONFIG_URL = r"{}/".format(API_URL)  # this is url for get all config
    GET_USER_TYPE_URL = r"{}/".format(API_URL)  # this is url for get user type
