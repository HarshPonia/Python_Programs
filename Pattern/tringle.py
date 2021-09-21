n = int(input("Enter the number"))
for i in range(0,n):
    for j in range(0,i+1):
        if j==0 or j==i:
            print("@",end = " ")
        else:
            print(" ",end = "")
    print("")