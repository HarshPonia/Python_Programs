def display(*x, sep=' ', end='\n'):  # x = 3, y = 6
    st_lst = list(map(str, x))
    f = sep.join(st_lst)
    print(f, end=end)
    

display(2, 4, 6, 7, 'amir', sep='\n', end='')
display('hello')