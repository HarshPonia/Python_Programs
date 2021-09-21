a = []
n = int(input("Enter the no. of element \n"))
for i in range(0,n):
    b = int(input("Enter the element\n"))
    a.append(b)
a.sort()
print(a[-1])
