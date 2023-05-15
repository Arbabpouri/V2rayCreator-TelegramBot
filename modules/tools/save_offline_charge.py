from json import loads, dumps
from os.path import isfile
from typing import Dict




if (isfile("./config/data.json") is False):
    with open("./config/data.json", "a+") as file:
        file.write(
            dumps({}, indent=4)
        )
        file.close()


class OfflineChargeData:
    
    
    def __init__(self, id: int) -> None:
        """_summary_

        Args:
            id (int): _description_
        """
        self.id = id
        self.path = "./config/data.json"
    

    def write(self, user_id: int, price: int) -> bool:
        """_summary_

        Args:
            user_id (int): _description_
            price (int): _description_

        Returns:
            bool: _description_
        """
        with open(self.path, "a+") as file:
            data = loads(file.read())
            data[str(self.id)] = {
                "user_id": user_id,
                "price": price,
                "enable": True,
                "status": "Waiting",
                "by": None
            }
            file.truncate()
            file.write(dumps(data, indent=4))
            file.close()
        return True
            

    def delete(self, admin_user_id: int, status: str) -> bool:
        """_summary_

        Args:
            admin_user_id (int): _description_
            status (str): _description_

        Returns:
            bool: _description_
        """
        with open(self.path, "a+") as file:
            data: dict = loads(file.read())
            if (str(self.id) in list(data.keys())
                and data[str(self.id)]["enable"]):

                data[str(self.id)]["enable"] = False
                data[str(self.id)]["status"] = str(status)
                data[str(self.id)]["by"] = admin_user_id
                file.truncate()
                file.write(dumps(data, indent=4))
                file.close()
                return True
            else:
                file.close()
                return False
    
    
    def read(self) -> bool | Dict[str, str | int | bool]:
        """_summary_

        Returns:
            bool | Dict[str, str | int | bool]: _description_
        """

        with open(self.path, "a+") as file:
            data: dict = loads(file.read())
            file.close()

        if (str(self.id) in list(data.keys())):    
            return data[str(self.id)]
        return False



