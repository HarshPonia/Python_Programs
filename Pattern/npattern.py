n = int(input("Enter the number"))
for i in range(0,n):
    for j in range(0,i+1):
        if j == 0:
            print("#",end = " ")
        else:
            print(" ", end = " ")
    for j in range(i,n+1):
        if j==n or j==i:
            print("@", end = " ")
        else:
            print(" ", end =" ")
    print(" ")

