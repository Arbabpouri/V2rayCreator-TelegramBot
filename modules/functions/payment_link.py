from config import Config


def create_payment_link(user_id: int, price: int) -> str:
    if (not str(user_id).isnumeric() or not str(price).isnumeric()):
        raise ValueError("user_id/price must be integer")
    
    return "{}/?userId={}&Price={}".format(Config.PAYMENT_DOMAIN, int(user_id), int(price))
