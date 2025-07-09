temperatures = [5, 12, 30, 8, 22, 26, 15, 7, 10, 28]

cold_days = []

warm_days = []

hot_days = []

for i in temperatures:
    if i < 10:
        cold_days.append(i)
    elif i >= 10 and i <= 25:
        warm_days.append(i)
    elif i > 25:
        hot_days.append(i)
    

print("orginal temperature:", temperatures, len(temperatures))
print("cold dyas:", cold_days, len(cold_days))

print("warm days", warm_days, len(warm_days))
print("hot days:", hot_days, len(hot_days))