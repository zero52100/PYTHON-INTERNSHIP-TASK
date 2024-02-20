def stackPUSH(stack, item):
    stack.append(item)
    print(item, "is inserted to stack")
def stackPOP(stack):
    if len(stack)==0:
        print("Stack is empty")
    else:
        item = stack.pop()
        print(item, "is removed")
def stackDISPLAY(stack):
    if  len(stack)==0:
        print("Stack is empty")
    else:
        print("Stack elements:", stack)
def stackTOP(stack):
    if  len(stack)==0:
        return None
    return stack[-1]
stack = []
while True:
    print("Stack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Top")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = int(input("Enter the item to push: "))
        stackPUSH(stack, item)
    elif choice == '2':
        stackPOP(stack)
    elif choice == '3':
        stackDISPLAY(stack)
    elif choice == '4':
        top_element = stackTOP(stack)
        if top_element is not None:
            print("Top element of the stack:", top_element)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice ! Please enter a valid entry.")
