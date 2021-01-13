import random
import math
import datetime
import platform as p

d = datetime.datetime.now()
print(d)
print(d.strftime("Date: %A, %d %b %Y\nTime: %I:%M:%S %p"))
print(p.system())
print(p.uname())
print(p.node())

z = 100/3
print(z)
print(f'{z:.2f}')