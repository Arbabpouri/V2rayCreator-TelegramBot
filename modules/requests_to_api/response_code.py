from enum import IntEnum, unique


@unique
class ResponseCode(IntEnum):
    SUCSESS = 0


@unique
class ResponseResult(IntEnum):
    USERNAME_ERROR = 11
    PASSWORD_ERROR = 12
