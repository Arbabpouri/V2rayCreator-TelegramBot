from config import Config

def create_payment_link(UserId: int, Price: int) -> str:
    return "{}/?userId={}&Price={}".format(Config.PAYMENT_DOMAIN, UserId, Price)