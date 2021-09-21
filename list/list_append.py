# appped :- append is used for add an element in list at the last position
#syntax:- var.append(obj)

#Example 1:-
lst = [1,2,3,4,5]
print(type(lst))
print('Before append = ',lst)
lst.append(6)
print('After append = ',lst)

# only one element can add using append 
# We can add list into a list using append

#Example 2:-
lst = ['hello ','hi']
print(type(lst))
print('Before append = ',lst)
lst.append(['How','Are','You'])
print('After append = ', lst)

# We can add any type of data using append

#Example 3:-
lst = ['hello',  'Ram','is','Going','to','school']
print(type(lst))

print('Before append = ',lst)
lst.append(1)
print('after append = ',lst)

print(lst)
