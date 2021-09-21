ch = int(input("Enter the number of class held"))
ca =int(input("enter the number of class attend"))
per = ca/ch*100
print("Attendence percentage = ", per)
if(per>=75):
    medical = input("if you have medical cause yes(Y) no(N)")
    if(medical=='N'):
        print("YES you are allowed in the exam")
    else:
        print("Sorry you are not allowed in the exam")