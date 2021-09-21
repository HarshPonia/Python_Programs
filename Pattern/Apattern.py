n = 8
for i in range(0,n):
    if i == 0:
        print(" ",end = "")
    print("@",end = "")
print("\r")
for i in range(0,n//2):
    print("@        @")
for i in range(0,n+2):
    print("@",end = "")
print("\r")

for i in range(0,n//2):
    print("@        @")