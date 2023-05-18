from enum import IntEnum, unique



@unique
class ResponseCode(IntEnum):
    SUCSESS = 0
    FAILURE = 1
    PARAMETER_ERROR = 2
    ADMIN_ALREADY_CREATED = 10
    ADMIN_NOT_FOUND = 11
    ADMIN_WRONG_PASSWORD = 12
    USER_DOES_NOT_EXIST = 30
    USER_ALREADY_EXIST = 31
    USER_TYPE_ERROR = 32
    LOW_AMOUNT = 40
    LOW_BALANCE = 41
    GETEWAY_AUTH_CODE_ERROR = 42
    DUPLICATE_VERIFY = 43
    VERIFY_HAS_PROBLEM = 44
    GATEWAY_NOK = 45
    PAYMENT_DOES_NOT_EXIST = 46
    SERVET_DOES_NOT_EXIST = 100
    SAME_SERVER_ALREADY_EXIST = 101
    SERVER_IS_FULL = 102
    CONFIG_TYPE_NOT_FOUND = 110
    CONFIG_DOES_NOT_EXIST = 120
    CONFIG_WAS_DISABLED = 121
    CONFIG_IS_ALREADY_ENABLE = 122
    ADD_NEW_CONFIG_PANEL_FAILUR = 130
    UPDATE_CONFIG_PANEL_FAILURE = 131
    REMOVE_CONFIG_PANEL_FAILURE = 132
    TELEGRAM_SEND_MESSAGE_ERROR = 200
