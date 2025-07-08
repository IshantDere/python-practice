numbers = [4, 7, 2, 4, 9, 10, 2, 3, 6, 7, 8]

unique_num = []
for i in numbers:
    if i not in unique_num:
        unique_num.append(i)
print("original list:", numbers)
print("without duplication :",unique_num)

even_num = []
odd_num = []

for i in unique_num:
    if i%2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)

even_num.sort(reverse=True)
odd_num.sort(reverse=True)

print("even numbers in desending order:", even_num)
print("odd numbers in desending order:", odd_num)