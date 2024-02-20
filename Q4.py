def input_matrix(rows, cols):
    matrix = []
    print("Enter the elements of the matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def mult(matrix1, matrix2):
    result = []

    if len(matrix1[0]) != len(matrix2):
        print("Matrix multiplication is not possible.")
        return result

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            row.append(0)
        result.append(row)

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

row1 = int(input("Enter the number of rows in Matrix 1: "))
col1 = int(input("Enter the number of columns in Matrix 1: "))
matrix1 = input_matrix(row1, col1)

row2 = int(input("Enter the number of rows in Matrix 2: "))
col2 = int(input("Enter the number of columns in Matrix 2: "))
matrix2 = input_matrix(row2, col2)

result = mult(matrix1, matrix2)

print("Matrix 1:")
for row in matrix1:
    print(row)

print("Matrix 2:")
for row in matrix2:
    print(row)

print("Result:")
for row in result:
    print(row)
