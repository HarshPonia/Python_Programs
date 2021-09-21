# def display(*x, sep=' ', end='\n'):  # x = 3, y = 6
#     st_lst = list(map(str, x))
#     f = sep.join(st_lst)
#     print(f, end=end)
    

# display(2, 4, 6, 7, 'amir', sep='\n', end='')
# display('hello')


# def student_info(name, section, roll_number, subject):
#     # logic
#     info = f'''
#         Name : {name}
#         Section : {section}
#         Roll Number: {roll_number}
#         subject : {subject} 
#     '''
#     return info

# # k = student_info('manish', 3, 'E', 'Python')  # positional argv
# # print(k)

# V = student_info( roll_number=34,  section='E', subject='Python Programming', name='ravi')  # function calling using keyword argv
# print(V)


# example 2: with  optional keyword arguments
# def student_info( **dct):
#     # logic
#     info = f'''
#         Name : {dct.get('name')}
#         Section : {dct.get('section')}
#         Roll Number: {dct.get('roll_number')}
#         subject : {dct.get('subject')} 
#     '''
#     return info
# V = student_info( subject='Python')  # function calling
# print(V)



# keyword arguments (optional)
def student_info( **var):
    # logic
    print(var)
    info = f'''
        Name : {var.get('name')}
        Section : {var.get('section')}
        Roll Number: {var.get('roll_number')}
        subject : {var.get('subject')} 
    '''
    return info

k = student_info( subject='math', name='ravi', cpi=8.5)
print(k)