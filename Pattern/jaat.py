n = 8
for i in range(0,n):
    print(" @",end = "")
for i in range(0,n+3):
    if(i>=6):
        print("@",end="")
    print("\r\t@")

for i in range(0,n):    
    if(i>=(n/2)-1):
        print("@",end= " ")
print("\n")



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
    
print("\n")
    
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
    
    
print("\n")


n = 5
for i in range(0,n*3+1):
    print("@",end = "")
print("\r")
for i in range(0,n+3):
    print("\t@")
