num1 = float(print("Enter first number: "))
op = input("Enter the operator: ")
num2 = float(print("Enter the second number: "))

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "*":
    print(num1 * num2)

elif op == "/":
    print(num1 / num2)

else:
    print("invalid operator")