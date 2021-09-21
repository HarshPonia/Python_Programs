length = 12

for p in range(0, length):
    for n in range(0, p + 1):
      print(end=" ")

    for n in range(p, length-1):  
      print("@", end=' ')
    print(" ")
for p in range(0, length):
    for n in range(0,p+1):
      print("@",end ='')
    print(" ")
    for n in range(p, length-1):
      print(end = " ")
    