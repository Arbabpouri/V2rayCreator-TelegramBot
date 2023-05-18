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
    result: Optional[GetAllConfigTypesList] = None


#
class OfflineCharge(BaseModel):
    user_id: int
    price: int
    enable: bool
    status: str
    by: Optional[str] = None



# 
class GetConfigResult(BaseModel):
    id: int
    name: str
    protocol: str
    serverName: str
    configTypeTitle: str
    numberOfUsers: int
    activeDays: int
    maxTraffic: int
    v2RayLink: str
    creationDate: str # TODO
    expiresDate: str # TODO
    clientUserId: int
    up: int
    down: int
    isEnable: bool

class GetConfig(BaseModel):
    status: int
    message: str
    result: Optional[GetConfigResult] = None


#
class GetUserConfigsResult(BaseModel):
    id: int
    name: str
    protocol : str
    serverName: str
    configTypeTitle: str
    numberOfUsers: int
    activeDays: int
    maxTraffic: int
    v2RayLink: str
    creationDate: str # TODO
    expiresDate: str # TODO
    clientUserId: int
    up: int
    down: int
    isEnable: bool


class GetUserConfigs(BaseModel):
    status: int
    message: str
    result: Optional[List[GetUserConfigsResult]] = None


#
class AddNewConfigResult(BaseModel):
    name: str
    protocol: str
    serverName: str
    configTypeTitle: str
    numberOfUsers: int
    activeDays: int
    maxTraffic: int
    v2RayLink: str
    creationDate: str # TODO
    expiresDate: str # TODO


class AddNewConfig(BaseModel):
    status: int
    message: str
    result: Optional[AddNewConfigResult] = None


#
class ChangeProtocolResult(BaseModel):
    name: str
    protocol: str
    serverName: str
    configTypeTitle: str
    numberOfUsers: int
    activeDays: int
    maxTraffic: int
    v2RayLink: str
    up: int
    down: int
    creationDate: str # TODO
    expiresDate: str # TODO


class ChangeProtocol(BaseModel):
    status: int
    message: str
    result: Optional[ChangeProtocolResult] = None


#
class ChangeServerResult(BaseModel):
    name: str
    protocol: str
    serverName: str
    configTypeTitle: str
    numberOfUsers: int
    activeDays: int
    maxTraffic: int
    v2RayLink: str
    up: int
    down: int
    creationDate: str # TODO
    expiresDate: str # TODO

class ChangeServer(BaseModel):
    status: int
    message: str
    result: Optional[ChangeServerResult] = None



#
class RenewakConfigResult(BaseModel):
    name: str
    protocol: str
    serverName: str
    configTypeTitle: str
    numberOfUsers: int
    activeDays: int
    maxTraffic: int
    v2RayLink: str
    up: int
    down: int
    creationDate: str # TODO
    expiresDate: str # TODO

class RenewakConfig(BaseModel):
    status: int
    message: str
    result: Optional[RenewakConfigResult] = None


#
class DeleteConfig(BaseModel):
    status: int
    message: str
    result: Optional[str] = None


#
class GetAllServerResult(BaseModel):
    id: int
    name: str
    limit: int
    activeConfigs: int

class GetAllServerList(BaseModel):
    servers: Optional[List[GetAllServerResult]] = None

class GetAllServer(BaseModel):
    statis: int
    message: str
    result: Optional[GetAllServerList] = None


#
class GetSettingsResult(BaseModel):
    minSellerAmount: int

class GetSettings(BaseModel):
    status: int
    message: str
    result: Optional[GetSettingsResult]


#
class GetUserInfoResult(BaseModel):
    balance: int
    referralerUserId: Optional[int] = None
    referrals: Optional[List[int]] = None
    precentage: int

class GetUserInfo(BaseModel):
    status: int
    message: str
    result: Optional[GetUserInfoResult] = None
