qty = int(input("Enter quantity\n"))
if(qty>1000):
    dis = qty*10/100
    total = qty-dis
    print("total cost= \n", total)
else:
    printf("No discount\n")