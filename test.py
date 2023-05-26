import requests

s = requests.post(
    "http://cnmellat.top/api/Auth/LogIn",
    data={
        "username": "MellatVpnAccount",
        "password": "AlienSardarMomeni2023",
    },
    verify=False)
print(s)