import time


a = 1000
b = 1000

import sys
print(sys.getrefcount(1000))    # 5 

time.sleep(5)   # 혹시 몰라서 5초 여유 둬봤음 ㅋㅋ
a = 1000
print(sys.getrefcount(1000))    # 5 --> 수 증가 X

time.sleep(5)
b = 1000
print(sys.getrefcount(1000))    # 5

print(a is b)   # True

c = 1000.0
print(sys.getrefcount(1000))    # 5
print(sys.getrefcount(1000.0))  # 4
print(a is c)   # False