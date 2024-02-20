def check_password(password):
    if len(password) < 8:
        return "Password is too short (minimum 8 characters)"
    
    lower_case = False
    upper_case = False
    digit = False
    special_char = False
    special_characters = ['_', '@', '$']
    
    for char in password:
        if char.islower():
            lower_case = True
        elif char.isupper():
            upper_case = True
        elif char.isdigit():
            digit = True
        elif char in special_characters:
            special_char = True
    
    missing = []
    
    if not lower_case:
        missing.append("lowercase alphabet")
    if not upper_case:
        missing.append("uppercase alphabet")
    if not digit:
        missing.append("number")
    if not special_char:
        missing.append("special character ( _ or @ or $ )")
    
    if lower_case and upper_case and digit and special_char:
        return "Password is valid"
    else:
        return "Invalid Password. Missing: {}".format(", ".join(missing))

password = input("Enter the password: ")
result = check_password(password)
print(result)
