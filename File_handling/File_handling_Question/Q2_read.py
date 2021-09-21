

f = open('addition.txt','r')
n = int(input("Enter number of line\n"))
for i in range(n):
    v = f.readline()
    print(v,f.tell())

f.close()

