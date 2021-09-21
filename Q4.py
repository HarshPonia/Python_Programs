salary = float(input("Enter salary\n"))
year = int(input("Enter the year of work\n"))
if(year>5):
    b = salary*5/100
    print("Your bonus = ", b)
else:
    print("Sorry!\n Your year of work is less than 5 years")