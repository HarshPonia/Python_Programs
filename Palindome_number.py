n = int(input("Enter a number\n"))
t = n
rev = 0
while n>0:
    d = n%10
    rev = rev*10+d
    n = n//10
if t == rev:
    print("Yes palindrome")
else:
    print("No")