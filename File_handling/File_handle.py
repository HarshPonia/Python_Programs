# File Handling in python:-  


# Demo Ex :- 
# f = open('hp.txt','r')
# f.write("who r u ")
# v = f.read()
# print(v)
# f.close()

#  Open() function:- open is use to open an exiting file in a object .  
#  Opens a file for reading, error if the file does not exist
# if file is not exiting then it will create new file with that name

# syntax of open():    var =  var.open(Filename, Mode)
# Mode :-  we have four mode 
# 1. 'r'(For thread operation):- it is use for read operation on txt file
# 2. 'w' 
# 3. 'a'
# 4. 'x'

# Example:-  


# f  =  open('hp.txt','w')
# f.write("Hii  This file is created by Harsh")

# f.close()


# Ex:- 2

# f = open('addition.txt')
# f2 = open('copy_addition.txt', 'w')
# f2.write(f.read())
# f2.close()
# f.close()

# ex:--
# f  = open('hp.txt','r+')

# data = f.read()  # it will read the entire data of the file
# print(data)
# f.close()



# Write a file 
# We use 'w' to write a new file 
# syntax:-   Variable_name.wrire(Enter the data)

# Ex :-
# f  = open('my_data.txt', 'w')
# v = "Name - Harsh Ponia\nCourse - B tech\nBranch - Computer science"
# f.write(str(v))
# f.close()







# Read the file
# Ex  :- 


# f =  open('Table.txt','r')
# data = f.read()
# print(data)
# f.close()

# Read by argument:-
# Ex :- 

# n = int(input("Enter the number of char to read"))
# f = open('my_data.txt', 'r')
# data = f.read(n)  # it will read 10 character..
# print(data)
# print(f.tell())         # it will give the cursur point 
# f.close()



# readline() :-  You can return one line by using the readline() method:-  it will read whole line at a time

# Ex:- 

# f = open('my_data.txt','r')
# v = f.readline()            # read  a line at a time
# print(v)
# print(f.tell())
# f.close()


#  By calling readline() two times, you can read the two first lines:

# Ex:- 

# f = open('Table.txt')
# data = f.readline()
# print(data)
# print(f.tell())
# print("\n")
# data1 = f.readline()
# print(data1)
# print(f.tell())



# readline by argument:- 
# f = open('table.txt', 'r')
# data = f.readline(20) # it will work on character
# print(data)


#  readlines():-  
f = open('table.txt', 'r')
data = f.readlines(30) # it will work on character
print(data)
