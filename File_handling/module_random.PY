import random
c =0
v = random.randrange(1,2000)
while True:
    n = int(input("Enter a number\n"))
    if n>v:
        print("Number is graeter\n")
    elif n<v:
        print("Number is smaller\n")
    else:
        print("Yes You got it")
        break 
    c+=1
print(c)   
