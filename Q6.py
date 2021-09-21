x = int(input("Enter the age of first person\n"))
y = int(input("Enter the age of second person\n"))
z = int(input("Enter the age of third person\n"))
if(x>y and x>z):
    print("x is oldest")
elif(y>z and y>x):
    print("y is oldest")
elif(z>x and z>y):
    print("z is oldest")

if(x<y and x<z):
    print("x is youngest")
elif(y<z and y<x):
    print("y is youngest")
elif(z<x and z<y):
    print("z is youngest")