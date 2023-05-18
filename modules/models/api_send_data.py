from typing import Optional, Dict
from config import Config
from pydantic import BaseModel


#
class AddUser(BaseModel):
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
# class 


#
# class