# import numpy as np
# f = open('addition.txt','r')
# v  = np.array(f.readlines())
# print(v,type(v))

f = open('addition.txt','r')
data_array = []
for line in f:
    data_array.append(line)
print(data_array)