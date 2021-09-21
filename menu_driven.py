n = int(input("Enter a number\n"))
m = int(input("enter second number\n"))
print("Menu\n\t1. Addition\n\t2. Subtraction\n\t3. Multipy\n\t4. division\n\t5. Moduus")
c = int(input("Enter your choice from menu\n"))
if c==1:
    print(m+n)
elif c==2:
    print(n-m)
elif c==3:
    print(m*n)
elif c==4:
    print(n/m)
elif c==5:
    print(n%m)
else:
    print("Wronng choice\n")
    