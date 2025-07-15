l1 = []
for i in range(26):
    l1.append(i)
# print(l1)

name = "Jimmy"

l2 = [] 
for i in range(1):
    l2.append(name)
# print(l2)

combine = l1 + l2

for i in combine:
    # print(i, '-->' ,j)
    
    if i == 20:
        print(name)
    else:
        print(i)