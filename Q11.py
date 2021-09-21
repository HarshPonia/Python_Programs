age = int(input("Enter age\n"))
sex = input("Enter sex m of f\n")
ms =  input("Enter the marital satus yes(Y) or no(N)")
if(sex == 'f'):
    print("she will work only urban areas.\n")
elif(sex == 'm' and age>20 and age<40):
    print("He may work anywhere\n")
elif(sex=='m' and age>40 and age<60):
    print("He will work in urban areas only\n")