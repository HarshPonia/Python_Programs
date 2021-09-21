f = open('file.txt','w')
f.write("how are you harsh")
f.close()

# f = open('file.txt','r')
# v = f.read()
# print(v)
# f.close()

f = open('file.txt','a+')
x = "i am fine"
f.write(x)
# v = f.read()
# print(v)
f.close()
f = open('file.txt','r')
v = f.read()
print(v)
f.close()
