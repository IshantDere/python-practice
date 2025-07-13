uppercase = 0
lowercase = 0
digit = 0
special_char = 0

text = "Hello123@World!"
for i in text:
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1
    elif i.isdigit():
        digit += 1
    else:
        special_char += 1

print("uppercase: ",uppercase)
print("lowercase: ",lowercase)
print("digits :",digit)
print("special character: ",special_char)