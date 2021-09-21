#check fil closed or not
f = open('addition.txt','r')
print(f.closed)
f.close()
print(f.closed)