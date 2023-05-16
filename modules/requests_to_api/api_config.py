from config import Config
from requests import post
from json import loads
from modules.requests_to_api.data_for_send import Data
from modules.requests_to_api.response_code import ResponseCode
from modules.models.models import GetToken


class ApiConfig:

    def __init__(self) -> None:
        pass


    @property
    def get_token(self) -> bool:
        """
            request to api for get jwt token for send token in headers
            if successful : write jwt token in config/token.txt
            else : return error type and exit in application
        """

        data = Data()
        req = post(url=Config.TOKEN, data=data.get_token)

        if (req.status_code != 200):
            del (data, req)
            return False
        
        result = GetToken(**loads(req.content))

        if (result.status == ResponseCode.SUCSESS):

            with open(r"./config/token.txt", "w+") as file:
                file.write(result.result.jwtToken)
            del (data, result)
            return True

        else:
            print(
                "Error : {}".format("Username is wrong" if (result.status == ResponseCode.USERNAME_ERROR) else \
                                    "Password is wrong" if (result.status == ResponseCode.PASSWORD_ERROR) else result.message)
            )
            exit()

    @property
    def get_prices_limit(self):
        '''
            request to api for get price limit
            manual users and seller users have bin diffrent price limit , so you need to find the price limit for each
        '''
        pass
