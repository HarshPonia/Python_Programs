# Set-->  set is used to store multiple value in a variable
# 1. -  Set is one of 4 built-in data types in Python used to store collections of data, 
# 2. -  the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# Sets are written with curly brackets{}.

# Ex-->
from typing import KeysView


theset = {'hello',2,'i','am',17,'year','old'}
print(theset)

# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.

# Once a set is created, you cannot change its items, but you can add new items.



# Duplicates Not Allowed

# Ex -->
theset = {'helle','hello','hi','helle','hi'}    # duplicates are not allowed in set
print(theset)                                   # output - helle,hi,hello
print(type(theset))
print(id(theset))

#data,integer,string --->

# Ex-->
s = {'hello','hii'}
s1 = {1,2,3,4,56,7,8,99}
s2 = {True,True,True,False}
print(s)
print(s1)
print(s2)


# Set Constructor
#Ex:--->
s = set(('Hi',2,'harsh','Hello'))
print(s)
print(type(s))


# Ex-->

s = {'He' , 'is','a','good boy','apple','He'}
print(s)
print(type(s))
print(len(s))
print(type(s))

#Access item in set:--> we can not access items by inndex or key 
# but we can access items by two methods 
# by for loop
# Ex:-->

s = {'HELLO','HII','TU','KON'}
for i in s:
    print(i ,end=" ")

# In function
x =  {'apple',1,'banana',2,'Orange',3}
print('banana' in x)

# We can  not change the items

# Add Items---> We use add() function to add a  item in set

#Syntax :-->  setname.add(item)
x = set(input().split())
n = int(input("enter number of items you want ot add inset"))
for i in n:
    x.add([int,input().split()])
print(x)


# Add a set:-->  We use update() function to adda set set in another set
# syntax:-->  set_name.update(set_var)
s  = {'hii',2,5}
s1 = {'hello','he',25}
s.update(s1)
print(s,type(s))
print(s1,type(s1))


# update:--> update can update other type of collection data in set.
# Ex:--
s  = {'hii',2,5}
lst = ['hi',1,2,3,4,5,6,7]
tple = ('helllo','what are u doing now')
dct = {'name':'harsh','roll':100+19}
# s.update(lst)
s.update(tple)
# print(lst,type(lst))
# s.update(tple)
# print(tple,type(tple))
s.update(dct)           # if we update a dictionary in a set.it will upadte the key in set. 
print(dct,type(dct))       
print('After update = ',s,type(s))


# Remove Item:--> we can use two function to remove an item in a set
# 1. Remove():--> it will remove item but if item is not exist in set it will generate an error.
# syntax:--> set_var.remove(item)
s = {'harsh','how','are','you'}
s.remove('harsh')
# s.remove('who') # it wil generate error
print(s,type(s))


# 2.:- discard():--> it will remove item but if item is not exist in set.
#  it will not generate any error.
# syntax:--> set_var.discard(item)

# Ex:-->
theset = {'set','in','python'}
theset.discard('in')
theset.discard('update') #  it wil not generate  any type of error
print(theset)
