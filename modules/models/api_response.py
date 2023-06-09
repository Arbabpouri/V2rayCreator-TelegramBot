from pydantic import BaseModel
from typing import List, Optional



# UserType and UserTypeResult classes are for the data received from the user type api
class UserTypeResult(BaseModel):
    type: int

class UserType(BaseModel):
    status: int
    message: str | None = None
    result: UserTypeResult | None = None


# AddUser class is for the data received from the add user api
class AddUser(BaseModel):
    status: int
    message: str | None = None
    result: str | None = None


# GetToken and GetTokenResult classes are for the data received from the get jwt token api
class GetTokenResult(BaseModel):
    jwtToken: str

class GetToken(BaseModel):
    status: int
    message: str | None = None
    result: GetTokenResult | None = None


# GetAllConfigTypes and GetAllConfigTypesList and GetAllConfigTypesResult classes are for the data received from the get all configs types api
class GetAllConfigTypesResult(BaseModel):
    id: int
    title: str
    numberOfUsers: int
    activeDays: int
    maxTraffic: int
    priceForManualUsers: int
    priceForSellerUsers: int

class GetAllConfigTypesList(BaseModel):
    configTypes: Optional[List[GetAllConfigTypesResult]] = []

class GetAllConfigTypes(BaseModel):
    status: int
    message: str | None = None
    result: GetAllConfigTypesList | None = None


#
class OfflineCharge(BaseModel):
    user_id: int
    price: int
    enable: bool
    status: str
    by: str | None = None



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
    creationDate: str 
    expiresDate: str 
    clientUserId: int
    up: int
    down: int
    isEnable: bool

class GetConfig(BaseModel):
    status: int
    message: str | None = None
    result: GetConfigResult | None = None


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
    creationDate: str 
    expiresDate: str 
    clientUserId: int
    up: int
    down: int
    isEnable: bool


class GetUserConfigs(BaseModel):
    status: int
    message: str | None = None
    result: Optional[List[GetUserConfigsResult]] = []


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
    creationDate: str 
    expiresDate: str 


class AddNewConfig(BaseModel):
    status: int
    message: str | None = None
    result: AddNewConfigResult | None = None


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
    creationDate: str 
    expiresDate: str 


class ChangeProtocol(BaseModel):
    status: int
    message: str | None = None
    result: ChangeProtocolResult | None = None


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
    creationDate: str 
    expiresDate: str 
class ChangeServer(BaseModel):
    status: int
    message: str | None = None
    result: ChangeServerResult | None = None



#
class RenewalConfigResult(BaseModel):
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
    creationDate: str 
    expiresDate: str 

class RenewalConfig(BaseModel):
    status: int
    message: str | None = None
    result: RenewalConfigResult | None = None


#
class DeleteConfig(BaseModel):
    status: int
    message: str | None = None
    result: str | None = None


#
class GetAllServerResult(BaseModel):
    id: int
    name: str
    limit: int
    activeConfigs: int

class GetAllServerList(BaseModel):
    servers: List[GetAllServerResult] | None = None

class GetAllServer(BaseModel):
    status: int
    message: str | None = None
    result: GetAllServerList = None


#
class GetSettingsResult(BaseModel):
    minSellerAmount: int

class GetSettings(BaseModel):
    status: int
    message: str | None = None
    result: GetSettingsResult |None = None


#
class GetUserInfoResult(BaseModel):
    balance: int
    referralerUserId: Optional[int] = 0
    referrals: Optional[List[int]] = []
    precentage: int

class GetUserInfo(BaseModel):
    status: int
    message: str | None = None
    result: GetUserInfoResult | None = None


class PaymentLink(BaseModel):
    status: int
    message: str | None = None
    result: str


#
class GetAllConfigsResult(BaseModel):
    id: int
    name: str
    protocol: str
    serverName: str
    configTypeTitle: str
    numberOfUsers: int
    activeDays: int
    maxTraffic: int
    v2RayLink: str
    creationDate: str
    expiresDate: str
    clientUserId: int
    up: int
    down: int
    isEnable: bool

class GetAllConfigs(BaseModel):
    status: int
    message: str | None = None
    result: List[GetAllConfigsResult] | list | None = None
