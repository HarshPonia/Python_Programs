# Write a python program to find the longest words.
f = open('addition.txt','r')
words  = f.read().split()
mx = len(max(words,key=len))
print([word for word in words if len(word) == mx])
 