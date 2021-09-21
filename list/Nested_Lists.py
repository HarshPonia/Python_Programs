lst = []
flst = []
n = int(input("Enter a number"))
for i in range(n):
    n = input()
    lst.append(n)
    for j in range(2):
        n = input()
        lst.append(n)
    flst.append(lst)
print(lst)
