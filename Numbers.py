# In python We have Three numbers
# 1. int
# 2. float 
# 3. Complex
# Ex 1:- 

a= 25
print(type(a))  #int
b = -30
print(type(b))  #int

# Ex 2:-
  
c = 1.0
print(type(c))   #float
d = -20.25
print((type(d)))   # float

# Ex 3:-

e = 2j
print(type(e))    # complex
f = -4+5j
print(type(f))    # complex




# Convert Numbers 

# int into float/complex
#  Ex 1:
 
a = float(a)
print(a)           # 25.00
print(type(a))    # float

# Ex 2:-

b = complex(b)    
print(b)            # 25+0j
print(type(b))


# float into int/complex

# Ex 3:-

c = int(c)
print(c)               # 1
print(type(c))          #int


# Ex 4:-

d = complex(int(d))
print(d)                # 1+0j
print(type(d))          #complex

# Complex Numbers can not be coverted into float or int
print("Hello,Darkness")