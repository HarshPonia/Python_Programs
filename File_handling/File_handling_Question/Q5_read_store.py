# Write a Python program to read a file line by line and store it into a list.

f = open('addition.txt','r')
ls = []
for line in f:
    # data = f.readlines()
    ls.append(line)
print(ls)
f.close()



# def file_read(fname):
#     with open(fname) as f:
#             #Content_list is the list that contains the read lines.     
#         content_list = f.readlines()
#         print(content_list)

# file_read('addition.txt')