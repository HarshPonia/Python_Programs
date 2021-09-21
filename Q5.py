m = int(input("Enter the marks\n"))
if(m>80):
    print("Grade A")
elif(m>60 and m<=80):
    print("Grade B")
elif(m>50 and m<=60):
    print("Grade C")
elif(m>45 and m<=50):
    print("Grade D")
elif(m>25 and m<=45):
    print("Grade E")
else:
    print("Grade F")
