from json import loads, dumps
from os.path import exists


if (exists("./config/data.json") is False):
    with open("./config/data.json", "a+") as file:
        file.write(
            dumps({}, indent=4)
        )
        file.close()


class OfflineChargeData:
    
    
    def __init__(self, id: int) -> None:
        self.id = id
    

    def write(self, user_id: int, price: int) -> bool:
        with open("./config/data.json", "a+") as file:
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
        with open("./config/data.json", "a+") as file:
            data: dict = loads(file.read())
            if (str(self.id) in list(data.keys())):
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
