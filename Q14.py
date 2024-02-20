def to_check(year):
     if year % 400 == 0:
        return True
     elif year % 100 == 0:
        return False
     elif year % 4 == 0:
        return True
     else:
        return False

user_input=int(input("Enter the year to check it is leap year or not")) 


if to_check(user_input):
    print(f"{user_input} is leap year")
else:
    print(f"{user_input} is not leap year")
