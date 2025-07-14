name = "john"
name1 = "harry"
mn = "larry"
ln = "musk"

l1 = []
for i in range(1):
    l1.append(name)
    l1.append(mn)
    l1.append(ln)
# print(l1)

l2 = []
for i in range(1):
    l2.append(name1)
    l2.append(mn)
    l2.append(ln)
# print(l2)

for i, j in zip(l1, l2):
    print(i, '-->' ,j)