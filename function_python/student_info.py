#function calling types:- 
# there are two type of function clling
# 1. calling by positional argument
# 2. calling by keyword argument

# 1. functional calling by positional argumnt
# Example 1:-

def student_info(name,section,roll_number,subject):

    info = '''
        Name : {name}
        Section : {section}
        roll Number : {roll_number}
        subject : {subject}
        '''
    return info
n,s,S,c = input().split()
v = student_info(n, s, S, c)  # functional calling by positional argument

print(v)




# 2. functional calling by keyword argument

# Example 2:-

def student_info(name,section,roll_number,subject):

    info = f'''
        Name : {name}
        Section : {section}
        roll Number : {roll_number}
        subject : {subject}
        '''
    return info

v = student_info(name = 'Harsh',roll_number = 119,subject = 'computer',section = 'c') # Functional calling by keyword argument 
print(v)







