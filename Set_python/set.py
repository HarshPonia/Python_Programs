# s = set(int,input().split())
# print(s)
x = set(input().split())
# print(x)
print(type(x))
n = int(input("enter number of items you want ot add inset"))
for i in range(n):
    x.add(frozenset(map(int, input().split())))

print(x)
print(type(x))