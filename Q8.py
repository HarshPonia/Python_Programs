ch = int(input("Enter the number of class held"))
ca =int(input("enter the number of class attend"))
per = ca/ch*100
print("Attendence percentage = ", per)
if(per>=75):
    print("YES you are allowed in the exam")
else:
    print("Sorry you are not allowed int the exam")