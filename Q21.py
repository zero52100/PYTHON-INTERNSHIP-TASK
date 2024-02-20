def remove_space(text):
    result=text.replace(" ",'')
    return result

user_input=input("Enter a string :")
result=remove_space(user_input)

if user_input==result:
    print("The string doesn't contain any whitespace.")
else:
    print(f"The string before removing whitespace {user_input}")
    print(f"The after removing whitespace {result}")
