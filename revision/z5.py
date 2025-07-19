# John = Charli
name = "John"
mn = "Jimmy"
ln = "Bolt"

l1 = []
for i in range(1):
    l1.append(name)
    l1.append(mn)
    l1.append(ln)
# print(l1)

for i in l1:
    if i == name:
        print("Charli")
    else:
        print(i)