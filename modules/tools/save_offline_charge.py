from uuid import uuid1


class OfflineChargeData:
    
    def __init__(self, id: int) -> None:
        self.id = id
    
    def write(self, user_id: int, price: int) -> bool:
        pass

    def delete(self) -> bool:
        pass

    def read(self) -> bool:
        pass