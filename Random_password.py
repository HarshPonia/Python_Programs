import random
lower =  "asdfghjklqwertyuiopzxcvbnm"
upper = "ASDFGHJKLQWERTYUIOPZXCVBNM"
digit =  "0123456789"
symbol = "!@#$%^&*()_+-=:><?|"
all = lower+upper+digit+symbol
length  = 16
password  = "".join(random.sample(all,length))
print(password)
