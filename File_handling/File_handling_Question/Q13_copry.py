f = open('lis.txt','r')
f1 = open('addition.txt','w')

f1.write(f.readline())
f.close()
f1.close()