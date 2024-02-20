def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    if len(queue) == 0:
        print("Queue is empty")
    else:
        queue.pop(0)
        print("item is dequeue")
def display(queue):
    if len(queue)==0:
        print("Queue is empty")
    else:
        print(queue)



queue = []

while True:
    print("Enter the operation")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter the option: "))

    if choice == 1:
        item = int(input("Enter the item to push: "))
        enqueue(queue, item)
    elif choice == 2:
        dequeue(queue)
    elif choice == 3:
        display(queue)
        
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please enter a valid entry.")
