l1 = []
for i in range(101):
    l1.append(i)
# print(l1)

l2 = []
for i in range(101):
    l2.append(100-i)
# print(l2)
for i, j in zip(l1,l2):
    print(i,'->',j)