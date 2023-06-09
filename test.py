from pytz import timezone
from datetime import datetime
a = timezone("Asia/Tehran")
b = datetime.now(a)
print(b)