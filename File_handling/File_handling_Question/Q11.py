import os
statinfo = os.stat('addition.txt')
print(statinfo)
print(statinfo.st_size)