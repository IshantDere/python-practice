def fact(a):
    ans = 1 
    for i in range (1, a+1):
        ans = ans * i
    return ans 
    
x = fact(2)
print(x)
    