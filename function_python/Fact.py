def fact(n):
    f = 1
    while(n>0):
        f = n*f
        n -= 1
    return f

n = int(input())
v = fact(n)
print(v)