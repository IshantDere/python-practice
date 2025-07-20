def cardlocate(card, query):
    location = 0
    while True:
        if card[location] == query:
            return location
        location += 1
        break
    return -1

#testcase - 1 
t1 = cardlocate([13, 11, 10, 7, 4, 3, 1 ,0], 2)
print(t1)
#testcase - 2
t2 = cardlocate([4, 2, 1, -1], 0)
print(t2)
