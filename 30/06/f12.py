def min_num(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
    
x = min_num(3, 8, 10)
print(x)