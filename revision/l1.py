numbers = [10, -5, 0, 3, -1, 7, 0, -8]

positive_numbers = []
negative_numbers = []

for i in numbers:
    if i > 0:
        positive_numbers.append(i)
    elif i < 0:
        negative_numbers.append(i)

print("positive numbers :",positive_numbers)
print(len(positive_numbers))

print("negative numbers :",negative_numbers)
print(len(negative_numbers))