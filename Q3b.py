rows = int(input("Enter the numner of row"))


for i in range(1, rows + 1): 
    for j in range(rows - i):
        print("  ", end="")
    for k in range(2 * i - 1):
        print("*", end=" ")

    print() 
