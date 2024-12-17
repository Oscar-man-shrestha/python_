# Matrix Addition
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

for row in result:
    print(row)

# Matrix Multiplication
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for row in result:
    print(row)

# Transpose of a Matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
transpose = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose[j][i] = matrix[i][j]

for row in transpose:
    print(row)

# Diagonal Sum of a Matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(len(matrix)):
    primary_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][len(matrix) - 1 - i]

print("Primary diagonal sum:", primary_diagonal_sum)
print("Secondary diagonal sum:", secondary_diagonal_sum)

# Create a Matrix of Zeros
rows = 3
cols = 3
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    matrix.append(row)

for row in matrix:
    print(row)

# Create a Matrix with Incremental Numbers
rows = 3
cols = 3
matrix = []
num = 1

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(num)
        num += 1
    matrix.append(row)

for row in matrix:
    print(row)

# Create a Matrix with Random Numbers
import random
rows = 3
cols = 3
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 10))
    matrix.append(row)

for row in matrix:
    print(row)

#practice for quiz

# Matrix Subtraction
matrix1 = [[5, 8, 3],
           [6, 7, 4],
           [9, 1, 2]]
matrix2 = [[3, 2, 1],
           [5, 4, 3],
           [7, 6, 5]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] - matrix2[i][j]

for row in result:
    print(row)

# Upper Triangle of a Matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if j >= i:
            result[i][j] = matrix[i][j]

for row in result:
    print(row)
