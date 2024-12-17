#important questions of CPS

# Generating Permutations of a List
from itertools import permutations
lst = [1, 2, 3]
perms = list(permutations(lst))
for perm in perms:
    for item in perm:
        print(item, end=' ')
    print()

# Multiplication Table for First N Numbers
N = 5
for i in range(1, N+1):
    for j in range(1, N+1):
        print(f"{i*j:2}", end=" ")
    print()

# Prime Factorization of Multiple Numbers
def prime_factors(num):
    factors = []
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

numbers = [60, 75, 90]
for num in numbers:
    print(f"Prime factors of {num}: {prime_factors(num)}")

# Generating a Chessboard Pattern
size = 8
for row in range(size):
    for col in range(size):
        if (row + col) % 2 == 0:
            print('W', end=' ')
        else:
            print('B', end=' ')
    print()

# Find Common Elements in Multiple Lists
lists = [[1, 2, 3, 4], [2, 3, 5, 6], [2, 3, 7, 8]]
common = lists[0]
for lst in lists[1:]:
    common = [x for x in common if x in lst]
print("Common elements:", common)

# Pascal's Triangle
def pascal_triangle(n):
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(prev[j-1] + prev[j])
            row.append(1)
        print(row)
        prev = row

pascal_triangle(5)

# Spiral Matrix
def spiral_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    top, bottom, left, right = 0, n - 1, 0, n - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    for row in matrix:
        print(row)

spiral_matrix(5)

# Magic Square Validation
def is_magic_square(matrix):
    n = len(matrix)
    s = sum(matrix[0])
    
    for row in matrix:
        if sum(row) != s:
            return False

    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != s:
            return False

    if sum(matrix[i][i] for i in range(n)) != s or sum(matrix[i][n-i-1] for i in range(n)) != s:
        return False

    return True

square = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
]

print("Is magic square:", is_magic_square(square))

# Word Search Puzzle Solver
def search_word(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(x, y, idx):
        if idx == len(word):
            return True
        if x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] != word[idx]:
            return False
        
        temp = board[x][y]
        board[x][y] = '#'
        found = (dfs(x+1, y, idx+1) or dfs(x-1, y, idx+1) or
                 dfs(x, y+1, idx+1) or dfs(x, y-1, idx+1))
        board[x][y] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    return False

board = [
    ['C', 'A', 'T'],
    ['X', 'Z', 'O'],
    ['M', 'E', 'W']
]
word = "CAT"
print("Word found:", search_word(board, word))

