numbers = [5, -3, 10, 0, -8, 7, 2, -1, 9]

non_negative_num = []
even_num = []
odd_num = []


for i in numbers:
    if i > 0:
        non_negative_num.append(i)
    if i%2 == 0 and i > 0:
        even_num.append(i)
    if i%2 == 1 and i > 0:
        odd_num.append(i)

# print(non_negative_num)
# print(even_num)
print(odd_num)

sum_even = sum(even_num)
# print(sum_even)
if len(odd_num) > 0:
    avg_num = round(sum(odd_num) / len(odd_num))

# print(avg_num)

print("original list:", numbers)
print("non negative numbers: ", non_negative_num)
print("even numbers: ", even_num)
print("sum of all even numbers: ",sum_even)
print("odd numbers: ", odd_num)
print("average of odd number: ", avg_num)