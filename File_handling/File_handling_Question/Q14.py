f = open('addition.txt','r')
f1 = open('lis.txt','r')
for line1,line2 in zip(f,f1):
    print(line1+line2)
