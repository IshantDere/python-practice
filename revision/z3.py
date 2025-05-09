l1 = []
for i in range(0, 26, 1):
    l1.append(i)
#  print(l1)

l2 = []
for i in range(25, 51, 1):
    l2.append(i)
#  print(l2)

l3 = []
for i in range(50, 76, 1):
    l3.append(i)

for i, j, k in zip(l1, l2, l3):
    # print(i, '<-->' ,j, '<-->' ,k)
    if i > 25:
        print(i)
    elif j > 25:
        print(j)
    elif k > 25:
        print(k)