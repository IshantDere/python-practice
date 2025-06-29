numbers = [10, 20, 30, 40, 50]

try:
    user_input = input("enter the index:")
    index = int(user_input)
    print(f"value at index {index} is {numbers[index]}")

except ValueError:
    print("invalid input ! please enter again")

except IndexError:
    print("invalid index ! please enter again")
    