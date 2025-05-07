name = "john"
middle_name = "henry"
ser_name = "sten"

l1 = []
for i in range(1):
    l1.append(name)
    l1.append(middle_name)
    l1.append(ser_name)
print(l1)

l2 = []
for i in l1:
    if i != ser_name:
        l2.append(i)
print(l2)