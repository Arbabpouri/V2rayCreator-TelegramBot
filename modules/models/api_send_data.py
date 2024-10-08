from typing import Optional
from pydantic import BaseModel
from config import Config


#
class AddNewUser(BaseModel):
    userId: int
    referralerUserId: int


#
class UserId(BaseModel):
    userId: int


#
class LogIn(BaseModel):
    username: Optional[str] = Config.USERNAME
    password: Optional[str] = Config.PASSWORD


#
class AddNewConfig(BaseModel):
    userId: int
    serverId: int
    configTypeId: int
    protocol: str
    isFree: Optional[bool] = False


#
class ChangeServer(BaseModel):
    configId: int
    targeterverId: int


#
class RenewalConfig(BaseModel):
    configId: int


#
class Headers(BaseModel):
    Authorization: str


class CryptoCharge(BaseModel):
    crypto_payment_type: Optional[int] = 0
    user_id: int
    toman_amount: int


class CryptoOnlinePurchase(BaseModel):
    crypto_payment_type: Optional[int] = 1
    user_id: int
    toman_amount: int
    server_id: int
    config_type_id: int


class CryptoGetStatus(BaseModel):
    price: int | float
