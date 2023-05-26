from requests import (post, get)
from json import loads
from modules.api.data_for_send import Data
from modules.enums.enums import ResponseCode
from modules.models.api_response import (GetToken,
                                         GetSettings,
                                         GetSettingsResult)
from modules.api.urls import ApiUrls


class ApiConfig:


    def __init__(self) -> None:
        self.urls = ApiUrls()
        self.headers = Data().headers


    @property
    def get_token(self) -> bool:
        """
            responseuest to api for get jwt token for send token in headers
            if successful : write jwt token in config/token.txt
            else : return error type and exit in application
        """

        data = Data().get_token
        response = post(url=self.urls.GET_TOKEN,
                        data=data,
                        verify=False)

        if (response.status_code != 200):
            print(f"\n\n{response}\n\nApi has no response")
            del (data, response)
            exit()
        
        result = GetToken(**loads(response.content))

        if (result.status == ResponseCode.SUCSESS):
            

            with open(r"./config/token.txt", "w+") as file:
                file.write(f"bearer {result.result.jwtToken}")
                file.close()
                
            ApiUrls.TOKEN = rf"bearer {result.result.jwtToken}"
            del (data, result)
            return True

        print(
            "Error : {}".format("Username is wrong" if (result.status == ResponseCode.ADMIN_NOT_FOUND) else \
                                "Password is wrong" if (result.status == ResponseCode.ADMIN_WRONG_PASSWORD) else result.status)
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
                
                return False

            elif (response.status_code == 401):

                del response
                self.get_token
                continue

            else:

                del response
                return False
