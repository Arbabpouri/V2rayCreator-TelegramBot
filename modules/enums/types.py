from enum import IntEnum, unique


@unique
class UserTypes(IntEnum):
    MANUAL = 0
    SELLER = 1
    MARKETER = 2