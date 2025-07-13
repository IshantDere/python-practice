multiple_3 = 0
multiple_5 = 0
multiple_3nd5 = 0

for i in range(1, 51):
    if i%3 == 0 and i%5 == 0:
        multiple_3nd5 += 1
    if i%3 == 0:
        multiple_3 += 1
    if i%5 == 0:
        print(i)
        multiple_5 += 1

print("multiple of 3:", multiple_3)
print("multiple of 5:", multiple_5)
print("multiple of 3 and 5:", multiple_3nd5)