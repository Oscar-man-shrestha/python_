#all about patterns....

# REGULAR PYRAMID
n = 5
i = 1
while i <= n:
    print(' ' * (n - i) + '*' * (2 * i - 1))
    i += 1

# INVERTED PYRAMID
n = 5
i = 0
while n - i > 0:
    print(' ' * i + '*' * (2 * (n - i) - 1))
    i += 1

# RIGHT-ALIGNED TRIANGLE
n = 5
i = 1
while i <= n:
    print(' ' * (n - i) + '*' * i)
    i += 1

# LEFT-ALIGNED TRIANGLE
n = 5
i = 1
while i <= n:
    print('*' * i)
    i += 1

# SQUARE SHAPE
n = 5
i = 0
while i < n:
    print('* ' * n)
    i += 1

# RECTANGLE
rows = 3
cols = 6
i = 0
while i < rows:
    print('* ' * cols)
    i += 1

# RHOMBUS
n = 5
i = 1
while i <= n:
    print(' ' * (n - i) + '*' * n)
    i += 1

# SQUARE WITH NUMBERS
n = 5
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(j, end='')
        j += 1
    print()
    i += 1

# RECTANGLE WITH NUMBERS
rows = 3
cols = 6
i = 1
while i <= rows:
    j = 1
    while j <= cols:
        print(j, end='')
        j += 1
    print()
    i += 1

# RHOMBUS WITH NUMBERS
n = 5
i = 1
while i <= n:
    print(' ' * (n - i), end='')
    j = 1
    while j <= n:
        print(j, end='')
        j += 1
    print()
    i += 1

# REGULAR NUMBER PYRAMID
n = 5
i = 1
while i <= n:
    print(' ' * (n - i), end="")
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1

# INVERTED NUMBER PYRAMID
n = 5
i = 0
while i < n:
    print(' ' * i, end="")
    j = 1
    while j <= n - i:
        print(j, end="")
        j += 1
    print()
    i += 1

# CENTERED NUMBER PYRAMID
n = 5
i = 1
while i <= n:
    print(' ' * (n - i), end="")
    j = 1
    while j < i:
        print(j, end="")
        j += 1
    j = i
    while j >= 1:
        print(j, end="")
        j -= 1
    print()
    i += 1

# FULL PYRAMID OF NUMBERS (SAME NUMBER)
n = 5
i = 1
while i <= n:
    print(' ' * (n - i), end="")
    j = 1
    while j <= (2 * i - 1):
        print(i, end="")
        j += 1
    print()
    i += 1



#------------------------------------------------------------------------------------------------

#using for....

# REGULAR PYRAMID
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# INVERTED PYRAMID
n = 5
for i in range(n):
    print(' ' * i + '*' * (2 * (n - i) - 1))

# RIGHT-ALIGNED TRIANGLE
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)

# LEFT-ALIGNED TRIANGLE
n = 5
for i in range(1, n + 1):
    print('*' * i)

# SQUARE SHAPE
n = 5
for i in range(n):
    print('* ' * n)

# RECTANGLE
rows = 3
cols = 6
for i in range(rows):
    print('* ' * cols)

# RHOMBUS
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * n)

# SQUARE WITH NUMBERS
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, end='')
    print()

# RECTANGLE WITH NUMBERS
rows = 3
cols = 6
for i in range(rows):
    for j in range(1, cols + 1):
        print(j, end='')
    print()

# RHOMBUS WITH NUMBERS
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    for j in range(1, n + 1):
        print(j, end='')
    print()

# REGULAR NUMBER PYRAMID
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()

# INVERTED NUMBER PYRAMID
n = 5
for i in range(n):
    print(' ' * i, end="")
    for j in range(1, n - i + 1):
        print(j, end="")
    print()

# CENTERED NUMBER PYRAMID
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i), end="")
    for j in range(1, i):
        print(j, end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# FULL PYRAMID OF NUMBERS (SAME NUMBER)
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i), end="")
    for j in range(2 * i - 1):
        print(i, end="")
    print()
