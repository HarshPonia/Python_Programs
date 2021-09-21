f1,f2=  map(int,input().split())
i1,i2 = map(int,input().split())
f = f1+f2
i = i1+i2
r = (i//12)+f
x = (i%12)
print("inch = ",x)
print("feet = ",r)