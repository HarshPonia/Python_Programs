n = int(input("Enter a number"))


f = open('Table.txt','w')
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f'{i*j}\t',end = "")
        f.write(str(i*j) + '\t')
    print()
    f.write('\n')
f.close()