from enum import IntEnum, unique



@unique
class ResponseCode(IntEnum):
    SUCSESS = 0
    USERNAME_ERROR = 11
    PASSWORD_ERROR = 12
    USER_NOT_FOUND = 30
    USER_ALREADY_EXISTS = 31
