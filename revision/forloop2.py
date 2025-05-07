l1 = []
for i in range(0, 101, 1):
    l1.append(i)
# print(l1)

total = 0
for i in l1:
    if i <= 25:
        total = total + i
    elif i >= 75:
        total = total + i

print(total)