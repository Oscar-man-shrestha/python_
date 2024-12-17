def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial(n)}")

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

print(sum_natural(5))

def palindrome(strr):
    if len(strr) < 1:
        return False
    if strr == strr[::-1]:
        return True
    else:
        return False

print(palindrome("racecar"))

def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1)

print(power(2, 3))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))

import re
string = "oscaro"
positions = [match.start() for match in re.finditer("o", string)]
print(positions)

def spiral(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    top, bottom, right, left = 0, n - 1, n - 1, 0

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    for row in matrix:
        print(row)

spiral(5)
