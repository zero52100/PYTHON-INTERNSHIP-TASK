def to_check(input):
    return input.isdigit()
text = input("Enter string: ")
if to_check(text):
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
