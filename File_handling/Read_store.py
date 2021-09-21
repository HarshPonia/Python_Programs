f = open('my_data.txt','r')
n = int(input())
ls = []
for i in range(n):
    data = f.readline()
    ls.append(data)
print(ls)
f.close()


