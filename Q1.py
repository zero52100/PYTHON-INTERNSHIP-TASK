def add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 + num2

def sub():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 - num2

def mult():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 * num2

def div():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

def floor_div():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        return num1 // num2
    else:
        return "Error: Floor division by zero"

def modulus():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        return num1 % num2
    else:
        return "Error: Modulus by zero"

def expon():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 ** num2

while True:
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Exponentiation")
    print("8. Exit")

    user_choice = int(input("Enter your choice (1-8): "))

    if user_choice == 8:
        print("Exiting the program.")
        break
    if user_choice == 1:
        
        print("Result:", add())
    elif user_choice == 2:
        print("Result:", sub())
    elif user_choice == 3:
        print("Result:", mult())
    elif user_choice == 4:
        print("Result:", div())
    elif user_choice == 5:
        print("Result:", floor_div())
    elif user_choice == 6:
        print("Result:", modulus())
    elif user_choice == 7:
        print("Result:", expon())
    else:
        print("Invalid choice !! Please enter a number between 1 and 8.")
