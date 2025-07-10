l1 = []
l2 = []
for i in range(1, 101, 1):
    l1.append(i)

n = len(l1)
for i in range(1, n):
    cur = l1[i]
    prev = l1[i-1]
    l2.append(cur + prev)
print(l2)