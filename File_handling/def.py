
f = open('tble.txt','w+')
n = int(input("Enter a nuber\n"))
for i in range(1,n+1):
        for j in range(1,n+1):
            v = i*j
            f.write(str(v))
            f.write('\n')
f.close()