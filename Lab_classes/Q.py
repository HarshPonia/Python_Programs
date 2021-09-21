s = input()
s = s.split()
c = 0
print(s)
for i in s:
    if len(i)>=2:
        if i[0]==i[-1]:
            c+=1

print(c)