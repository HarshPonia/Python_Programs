
#   Write a Python program to count the frequency of words in a file.

from collections import Counter
f = open('addition.txt','r')
v = Counter(f.read().split())
print(v)