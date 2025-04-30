is_male = False
is_tall = False

if is_male or is_tall:
    print("you are a tall male")
elif is_male or not(is_male):
    print("you are a short male")
elif not(is_tall) or is_tall:
    print("you are not a male but are tall")   
else:
    print("you are not a male and not tall")