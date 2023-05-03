from typing import Optional, Dict
from config import Config


class Data:


    def __init__(self, user_id: Optional[int] = None, referraler: Optional[int] = 0) -> None:
        '''
            user id must be integer or None
        '''
        self.user_id = user_id
        self.referraler = referraler


    @property
    def add_user(self) -> Dict[str, int]:

        '''
            example: {
                "user_id": 123456789,
                "referraler": 987654321
            }
        '''
        
        return {
            "userId": int(self.user_id),
            "referralerUserId": int(self.referraler)
        }
    

    @property
    def userId(self) -> Dict[str, int]:

        '''
            example: {
                "userId": 123456789
            }
        '''

        return {
            "userId": int(self.user_id)
        }
    
    
    @property
    def get_token(self) -> Dict[str, str]:

        '''
            example : {
                "username": "admin",
                "password": "password"
            }
        '''

        return {
            "username": Config.USERNAME,
            "password": Config.PASSWORD,
        }

    
    