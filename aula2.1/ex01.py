from datetime import datetime
from zoneinfo import ZoneInfo

x = datetime(2026, 5, 1)
print(x)
print(type(x))

y = datetime(2026, 5, 19, 14, 30, 0)
print(y)
print(y.day)
print(y.month)
print(y.year)
print(y.hour)
print(y.minute)
print(y.second)
print(y.date())
print(y.time())
print(y.weekday())

#from zoneinfo inport ZoneInfo
#z = datetime.now(ZoneInfo("America/Sao_Paulo"))
z = datetime.now()
print(z)
print(z.strftime("%d/%m/%Y, %H/%M/%S"))
print(z.strftime("%d/%m/%y"))
print(z.strftime("%d/%m/%y, %a"))
print(z.strftime("%d/%m/%y, %A %B"))