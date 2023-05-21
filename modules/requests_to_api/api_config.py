from config import Config
from requests import (post, get, put, delete)
from json import loads
from modules.requests_to_api.data_for_send import Data
from modules.enums.response_code import ResponseCode
from modules.models.api_response import (GetToken,
                                         GetSettings,
                                         GetSettingsResult)
from modules.requests_to_api.urls import ApiUrls
from modules.requests_to_api import APIS


class ApiConfig:


    def __init__(self) -> None:
        self.urls = ApiUrls()
        self.headers = self.headers


    @property
    def get_token(self) -> bool:
        """
            responseuest to api for get jwt token for send token in headers
            if successful : write jwt token in config/token.txt
            else : return error type and exit in application
        """

        data = Data()
        response = post(url=self.urls.TOKEN,
                        data=data.get_token,
                        headers=self.headers)

        if (response.status_code != 200):
            del (data, response)
            return False
        
        result = GetToken(**loads(response.content))

        if (result.status == ResponseCode.SUCSESS):

            with open(r"./config/token.txt", "w+") as file:
                file.write(f"bearer {result.result.jwtToken}")
                
            ApiUrls.TOKEN = f"bearer {result.result.jwtToken}"
            del (data, result)
            return True

        else:
            print(
                "Error : {}".format("Username is wrong" if (result.status == ResponseCode.ADMIN_NOT_FOUND) else \
                                    "Password is wrong" if (result.status == ResponseCode.ADMIN_WRONG_PASSWORD) else result.message)
            )
            exit()


    @property
    def get_prices_limit(self) -> GetSettingsResult | bool:
        """
            responseuest to api for get price limit
            manual users and seller users have bin diffrent price limit , so you need to find the price limit for each
        """
        for i in range(2):
            
            response = get(url=self.urls.GET_SETTINGS,
                           headers=self.headers)
            
            if (response.status_code == 200):

                result = GetSettings(**loads(response.content))
                del response

                if (result.status == ResponseCode.SUCSESS):

                    return result.result

            elif (response.status_code == 401):

                del response
                APIS.config_api().get_token

            else:

                del response
                return False
