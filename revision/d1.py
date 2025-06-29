numbers = [10, 20, 30, 40, 50]
try:
    user_input = input("enter the index: ")
    index = int(user_input)
    # print("value of index {} is {}".format(index, numbers[index]))
    print(f"value at index {index} is {numbers[index]}")
except ValueError:
    print("invalid input, enter again.")
except IndexError:
    print("invalid index, enter again.")