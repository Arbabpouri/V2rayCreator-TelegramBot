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
                "price": price
            }
            file.truncate()
            file.write(dumps(data, indent=4))
            file.close()

        return True
            

    def delete(self) -> bool:
        with open("./config/data.json", "a+") as file:
            data: dict = loads(file.read())
            if (str(self.id) in list(data.keys())):
                del data[str(self.id)]
                file.truncate()
                file.write(dumps(data, indent=4))
                file.close()
                return True
            else:
                file.close()
                return False
