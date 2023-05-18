from typing import Optional, Dict
from config import Config
from modules.models.api_send_data import (AddNewUser,
                                          UserId,
                                          LogIn,)


class Data:


    def __init__(self, user_id: Optional[int] = None, referraler: Optional[int] = 0) -> None:
        """
            user id must be integer or None
        """
        self.user_id = user_id
        self.referraler = referraler


    @property
    def add_user(self) -> Dict[str, int]:

        """
            example: {
                "user_id": 123456789,
                "referraler": 987654321
            }
        """

        if (not str(self.user_id).isnumeric()): raise ValueError("user_id must be a number")

        data = AddNewUser(userId=int(self.user_id),
                          referralerUserId=int(self.referraler))
        
        return data.dict()
    

    @property
    def userId(self) -> Dict[str, int]:

        """
            example: {
                "userId": 123456789
            }
        """
        if (not str(self.user_id).isnumeric()): raise ValueError("user_id must be a number")

        data = UserId(userId=int(self.userId))

        return data.dict()
    
    
    @property
    def get_token(self) -> Dict[str, str]:

        """
            example : {
                "username": "admin",
                "password": "password"
            }
        """
        data = LogIn(username=Config.PASSWORD, password=Config.PASSWORD)
        return data.dict()

    
    #TODO: this function should completely
    def balance_increase(self, price) -> Dict[str, int]:
        """_summary_

        Args:
            price (_type_): _description_

        Raises:
            ValueError: _description_

        Returns:
            Dict[str, int]: _description_
        """

        return {
            "userId": self.user_id,
            "price": int(price)
        }
