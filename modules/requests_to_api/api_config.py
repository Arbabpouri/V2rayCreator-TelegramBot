from config import Config
from requests import (post, get, put, delete)
from json import loads
from modules.requests_to_api.data_for_send import Data
from modules.enums.response_code import ResponseCode
from modules.models.api_respons import GetToken
from modules.requests_to_api.urls import ApiUrls


class ApiConfig:


    def __init__(self) -> None:
        self.Urls = ApiUrls()


    @property
    def get_token(self) -> bool:
        """
            responsiveuest to api for get jwt token for send token in headers
            if successful : write jwt token in config/token.txt
            else : return error type and exit in application
        """

        data = Data()
        responsive = post(url=self.Urls.TOKEN, data=data.get_token)

        if (responsive.status_code != 200):
            del (data, responsive)
            return False
        
        result = GetToken(**loads(responsive.content))

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
    def get_prices_limit(self):
        """
            responsiveuest to api for get price limit
            manual users and seller users have bin diffrent price limit , so you need to find the price limit for each
        """
        
        pass

    