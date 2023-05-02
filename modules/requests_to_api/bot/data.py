from typing import Optional, Dict

class Data:
    def __init__(
            self,
            user_id: Optional[int] = None,
            referraler: Optional[int] = 0,
        ) -> None:
        '''
            user id must be integer or None
        '''
        self.user_id = user_id
        self.referraler = referraler


    @property
    def add_user(self) -> Dict[str, int]:
        
        return {
            "userId": int(self.user_id),
            "referralerUserId": int(self.referraler)
        }
    

    @property
    def userId(self) -> Dict[str, int]:

        return {
            "userId": int(self.user_id)
        }
    
    