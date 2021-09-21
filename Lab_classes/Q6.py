# # # a = [1,2,3]
# # # c = 0
# # # for i in range(3):
# # #     for j in range(3):
# # #         for k in range(3):
# # #             # if a[i]!=a[k]:
# # #             c+=1
# # #             print(a[i],a[j],a[k])
# # # print(c)
# # # print(type(type(int)))
# n = int(input())
# for i in range(0,n+1):
#     for j in range(i):
#         print(i,end = "")
#     print()

#m,n = map(int,input().split())
# # x = m^n
# # s = m+n
# # if x==s:
# #     print("'Valentine Match'")
# # else:
# #     print("None")

# n = int(input())
# c = 0
# x = n
# while x!=6174:
#     d = list(str(x))
#     d.sort(reverse=True)
#     if len(d)<4:
#         d.append('0')
#     a = int("".join(d))
#     d.reverse()
#     b = int("".join(d))
#     x = a-b
#     c+=1
# print(c)

n =  int(input())
c = 0 
x = n
while x!=6174:
    d = list(str(x))
    d.sort(reverse=True)
    a = int(d)
    d.reverse()
    b = int(d)
    c = a-b
    c+=1
print(c)