from enum import IntEnum, unique


class Limit:
    LIMIT = {}


@unique
class Step(IntEnum):
    GET_CUSTOM_CHARGE_ONLINE = 0
    GET_CUSTOM_CHARGE_OFFLINE = 1
    GET_CUSTOM_CHARGE_CRYPTO = 2
    GET_EVIDENCE = 3
