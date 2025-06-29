data = [10, "hello", 25, 44, None, 67, 100, "42"]
even_num = []
for i in data:
    try:
        if i%2 == 0:
            even_num.append(i)
    except:
        pass

print(even_num)