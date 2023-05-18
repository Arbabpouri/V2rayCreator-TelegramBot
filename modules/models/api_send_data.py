from typing import Optional
from pydantic import BaseModel


#
class AddNewUser(BaseModel):
    userId: int
    referralerUserId: int


#
class UserId(BaseModel):
    userId: int


#
class LogIn(BaseModel):
    username: str
    password: str


#
class AddNewConfig(BaseModel):
    userId: int
    serverId: int
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
