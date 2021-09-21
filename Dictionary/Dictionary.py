
"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List:--> is a collection which is ordered and changeable. Allows duplicate members.
Tuple:---> is a collection which is ordered and unchangeable. Allows duplicate members.
Set---> is a collection which is unordered and unindexed. No duplicate members.
Dictionary--->  is a collection which is ordered and changeable. No duplicate members.
When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, and, 
it could mean an increase in efficiency or security.



# Dictionary :-  A dictionary is a mutable  and unordered collection data type

with a pair of keys  and value
--> Each key is seprated from it's value by a colon {:}
--> As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""
# Demo:-  
 
from io import DEFAULT_BUFFER_SIZE


Dct = {'Name':'Harsh Ponia','Sec':'c','branch':'Computer science','college':'GLA UNIVERSITY'}
print(Dct)
print(Dct['college'])
print(Dct['branch'])


#  Empty Dictinary:- 
# Type 1:-
dct = {}
print(dct)
print(type(dct))

# Type 2:-
d = dict()
print(d,type(d))

# Example 1:-
d = {
    'name': 'Harsh',
    'year': 2021,
    'sub': 'python',
    'program':"Dictionary",
    'year':2020             #  Duplicate values will overwrite existing values:
}

print(d)


# Dictionary length:- 
# len(Name_of_dictionary)
# Ex 1:- 
d = {
    'name': 'Harsh',
    'year': 2021,
    'sub': 'python',
    'program':"Dictionary",
    'year':2020             #  Duplicate values will overwrite existing values:
}

print(d)
print(len(d))



# Accessing element in Dictionary by key :--->  You can access the items of a dictionary by referring to its key name, inside square brackets:

# Ex:-

dic = {

    'brand':'honda',
    'modal':'Activa',
    'year':2017,
    'owner':'Prakash singh',
    'vahical_number':'UP 86 W 3468',
    'date_of_purchase': '29 may',
    'chalan': 'None',
    'accident':4
}
print(dic['brand'])
print(dic['date_of_purchase'])
print(dic['owner'])

# If  enter a key which is not exists  in dictionary. it will give error



# Access element by Using  get() keys:---> 

# Ex:-->
dic = {

    'brand':'honda',
    'modal':'Activa',
    'year':2017,
    'owner':'Prakash singh',
    'vahical_number':'UP 86 W 3468',
    'date_of_purchase': '29 may',
    'chalan': 'None',
    'accident':4
}
v = dic.get("modal")
print(v)


x = dic.get("harsh")
print(x)

# Get all key of the dictionary :--->

























