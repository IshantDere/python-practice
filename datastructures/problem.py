def cardlocate(card, query):
    location = 0
    while True:
        if card[location] == query:
            return location
        location += 1
        
    return -1

#testcase - 1 
print(cardlocate([13, 11, 10, 7, 4, 3, 1 ,0], 2))
#testcase - 2
print(cardlocate([4, 2, 1, -1], 4))
#testcase - 3
print(cardlocate([3, -1, -9, -127], -127))