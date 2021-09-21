#  Q.   Get a list of name as an input from the user and make the first letters in caps and print each word as a list



Name = []

print("\nEnter names : ")

for i in range(0,n):

   x = input()

   Name.append(x)

   

print("\nNames are : ")

for i in range (0,n):

   print(Name[i].capitalize())

