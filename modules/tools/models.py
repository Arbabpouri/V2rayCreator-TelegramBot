from pydantic import BaseModel
from typing import List, Optional



# UserType and UserTypeResult classes are for the data received from the user type api
class UserTypeResult(BaseModel):
    type: int

class UserType(BaseModel):
    status: int
    message: str
    result: UserTypeResult = None


# AddUser class is for the data received from the add user api
class AddUser(BaseModel):
    status: int
    message: str
    result: str


# GetToken and GetTokenResult classes are for the data received from the get jwt token api
class GetTokenResult(BaseModel):
    jwtToken: str

class GetToken(BaseModel):
    status: int
    message: str
    result: GetTokenResult = None


# GetAllConfigTypes and GetAllConfigTypesList and GetAllConfigTypesResult classes are for the data received from the get all configs types api
class GetAllConfigTypesResult(BaseModel):
    id: int
    title: str
    numberOfUsers: int
    activeTime: int
    maxTraffic: int
    priceForManualUsers: int
    priceForSellerUsers: int

class GetAllConfigTypesList(BaseModel):
    configTypes: List[GetAllConfigTypesResult]

class GetAllConfigTypes(BaseModel):
    status: int
    message: str
    result: GetAllConfigTypesList = None


#
class GetUserConfigTypes(BaseModel):
    pass


class OfflineCharge(BaseModel):
    user_id: int
    price: int
    enable: bool
    status: str
    by: Optional[str] = None
