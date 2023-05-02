from typing import Optional, Dict
from config import Config


class Data:
    def __init__(self) -> None:
        self.user_name: str = Config.USERNAME
        self.password: str = Config.PASSWORD

    @property
    def get_token(self) -> Dict[str, str]:
        '''
            
        '''
        return {
            "username": self.user_name,
            "password": self.password,
        }
