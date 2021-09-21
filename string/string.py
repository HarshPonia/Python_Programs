# # # String:- string is the set of character 
# # # In python string surrounded by either single quotation  or doule qoutation mark

# #Example 1:-
# print('hello')
# print("hi")
# print('''hello''')
# print("""hi""")



# # # assign string to a vriable

# # # Example 2 :- 

# a= "hello"
# print(a)
# b = 'hello'
# print(b)
# c = """hello"""
# print(c)
# d = '''Hello'''
# print(d)
# e = '"hello"'
# print(e)
# f = "hello'hello'"
# print(f)

# # # Example 3:-
# a = '''\thello every one \n\ti hope you all are  good \n\tToday we are learning python string\n\tPython string is a very important'''
# print(a)
# b = """\thello every one \n\ti hope you all are  good \n\tToday we are learning python string\n\tPython string is a very important"""
# print(b)

# # # String as Array

# # # python has no Arraay type data type 
# # # In python string work as an array on character like:- a = hello (string have index numbers i.e.= h- 0, e- 1,l- 2,l-3,o-4) this is the index in python string
# # # But it work on characters

# # # Example 4:-

a =  "hello everyone"
print(a[0])
print(a[6])
print(a[10])

# # # Looping with string

# # # We can work with loop on string. same like as array

# # # example 5:-
# # for i in "i am a computer":
# #     print(i, end = "")

# # # Example 6:-
# # a = "अब ना मैं हूँ, ना बाकी हैं ज़माने मेरे​\nफिर भी मशहूर हैं शहरों में फ़साने मेरे​\nज़िन्दगी है तो नए ज़ख्म भी लग जाएंगे​\nअब भी बाकी हैं कई दोस्त पुराने मेरे"
# # print(a)
# # print(len(a))
# # re = list(range(10))
# # print(re)


# # # Lenght of string:-

# # # Example:-
# # a = "Hello friends, \nhow are you.\nI hope you all are good"
# # print(len(a))

# # # Modify the string:- 

# # # Upper:-  it will Covert All string into Upper case letter
# # # Ex 1 :-
# # x = "Hello, World"
# # print(x.upper())

# # # Lower:- it will covert All string into Lower  case Letter
# # y =  "Hii my name is harsh"
# # print(y.lower())

# # # Remove White spaces:- It will Remove all the spaces after string
# # z = "hello everyone             "
# # print(z.strip())

# # # Replace string:-- It will  replace the string

# # # Ex 1:- 
# # a =  "Think positive"
# # print(a.replace(" ", "_"))


# # String Methods:-
# """

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
# """


# # 1. capitalize() :- Converts the first character to upper case
# # The capitalize() method returns a string where the first character is upper case.
# # Syntax :- string.capitalize()

# # # Ex 1:-
# x = "hELLO Boys how are You"
# x = x.capitalize()
# print(x)

# # 2. casefold() = Converts string into lower case
# # lower() :-  it is also use for convert the string into lower case
# # syntax :- string.casefold()
# x = "hELLO Boys how are You"
# x = x.casefold()
# print(x)

# # 3. center()	Returns a centered string
# #The center() method will center align the string, using a specified character (space is default) as the fill character.

# #Syntax:-  string.center(length, character)

# # Ex 1:-
# x = "Harsh"
# x = x.center(20)
# print(x)

# # Ex2:- 
# x = "Harsh"
# x = x.center(20,'N')
# print(x)


# # 4. count():-  The count() method returns the number of times a specified value appears in the string.

# # Syntax :- string.count(value, start, end)

# # Ex:- 
# x = " My name is Harsh. My friend name is Rishabh.My friend nis Khargosh"
# print(len(x))
# x= x.count("My",)
# print(x)



