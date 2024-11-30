# Input dimensions for Matrix A
rows_a = int(input("Enter the number of rows in Matrix A: "))
cols_a = int(input("Enter the number of columns in Matrix A: "))

matrix_a = []
for i in range(rows_a):
    row = []
    for j in range(cols_a):
        element = int(input(f"Element [{i + 1}][{j + 1}]: "))
        row.append(element)
    matrix_a.append(row)

# Input dimensions for Matrix B
rows_b = int(input("Enter the number of rows in Matrix B: "))
cols_b = int(input("Enter the number of columns in Matrix B: "))

# Check if multiplication is possible
while cols_a != rows_b:
    print(f"Error: The number of columns in Matrix A ({cols_a}) must equal the number of rows in Matrix B ({rows_b}).")
    rows_b = int(input("Enter the number of rows in Matrix B: "))
    cols_b = int(input("Enter the number of columns in Matrix B: "))

# Input Matrix B
matrix_b = []
print("Enter the elements of Matrix B:")
for i in range(rows_b):
    row = []
    for j in range(cols_b):
        element = int(input(f"Element [{i + 1}][{j + 1}]: "))
        row.append(element)
    matrix_b.append(row)

# Initialize the result matrix
result_matrix = [[0] * cols_b for _ in range(rows_a)]

# Perform matrix multiplication
for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a):
            result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
print(type(result_matrix))
# Print the result
print("Resultant Matrix:")
for row in result_matrix:
    for value in row:
        print(value, end=' ')  # Print each value in the row
    print()  # Print
