numbers = [10, 15, 22, 33, 40, 55, 60]

even_num = 0
odd_num = 0

for i in numbers:
    if i%2 == 0:
        even_num += 1
    else:
        odd_num += 1


print("even numbers =", even_num)
print("odd numbers =", odd_num)