def check(a):
    if a > 0:
        return "positive"
    elif a < 0:
        return "negative"
    else: 
        return "zero"
    
x = check(0)
print(x)