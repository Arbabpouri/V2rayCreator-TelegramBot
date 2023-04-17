from config import Config


def create_payment_link(user_id: int, price: int) -> str:
    return "{}/?userId={}&Price={}".format(Config.PAYMENT_DOMAIN, user_id, price)
