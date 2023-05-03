from pydantic import BaseModel


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