import random
f = open('addition.txt','r')
lines = f.read().splitlines()
print(random.choice(lines))