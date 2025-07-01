grades = [85, 42, 77, 90, 35, 68, 49, 58, 100, 23]

pass_list = []
fail_list = []

for i in grades:
    if i >= 50:
        pass_list.append(i)
    elif i < 50:
        fail_list.append(i)
pass_list.sort()

print ("original grade :", grades)
print("passing grade :", pass_list)
print("failing_list :", fail_list)
print("number of passed", len(pass_list))
print("number of failing", len(fail_list))