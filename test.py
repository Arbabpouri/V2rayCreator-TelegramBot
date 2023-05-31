from datetime import date, datetime, timedelta

a = datetime(2023, 2, 2)
b = datetime(2022, 1, 1)
c = a - b

print(c.max)