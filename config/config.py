class BotConfig:

    def __init__(self) -> None:
        # BOT Config
        self.API_ID = 3359959  # Telegram Api ID , you can get it from telegram website
        self.API_HASH = "fc809b5d42bdac477f9ac9b56383a699"  # Telegram Api Hash , you can get it from telegram website
        self.BOT_TOKEN = "5867054982:AAH6SDlVaeULkaw5WF2aJSe3TiCvvMK5qq8"   # Bot Token,you can get it from @BotFather
        self.BOT_USERNAME = "V2rayCreatorBot"  # without the @ , example : V2rayCreatorBot
        self.SESSION_NAME = "bot"  # string
        self.USER_CHARGE = [50000, 100000, 150000, 200000]  # T
        self.SELLER_CHARGE = [500000, 1000000, 1500000, 2000000]  # T
        self.MIN_USER_CHARGE = 25000  # T , for min charge by manual user
        self.MIN_SELLER_CHARGE = 500000  # T , for min charge by seller user

        # API Config
        self.PAYMENT_DOMAIN = "127.0.0.1"  # payment url for buy
        self.API_URL = "0.0.0.0"  # this is url for requesting
        self.USERNAME = ""  # username for login to api for get token
        self.PASSWORD = ""  # password for login to api for get token
        self.GET_TOKEN_URL = r"{}/".format(self.API_URL)  # this is url for get token for request to api
        self.GET_USER_URL = r"{}/".format(self.API_URL)   # this is url for get user
        self.ADD_USER_URL = r"{}/".format(self.API_URL)  # this is url for add user
        self.GET_ALL_CONFIG_URL = r"{}/".format(self.API_URL)  # this is url for get all config
        self.GET_USER_TYPE_URL = r"{}/".format(self.API_URL)  # this is url for get user type

