for i in range(100):
    if i== 78:
        break
    print(i)

even = []
odd  = []
for i in range(1,50000000):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("List of even number upto 50 = ",even)
print("List of Odd numbers upto  50 = ", odd)
