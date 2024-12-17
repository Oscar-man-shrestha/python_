# 1. Largest of Three Numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 > num2:
    if num1 > num3:
        print("The largest number is:", num1)
    else:
        print("The largest number is:", num3)
else:
    if num2 > num3:
        print("The largest number is:", num2)
    else:
        print("The largest number is:", num3)

# 2. Even Numbers Between 1 and 50
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# 3. Odd Numbers Between 1 and N
n = int(input("Enter a positive integer value for N: "))
for i in range(1, n + 1, 2):
    print(i)

# 4. Sum of Series 1 + 2 + 3 + ... + N
n = int(input("Enter the value of N: "))
sum_series = sum(range(1, n + 1))
print("The sum of the series 1 + 2 + ... + N is:", sum_series)

# 5. Sum of Odd Series 1 + 3 + 5 + ... + N
n = int(input("Enter the value of N (positive odd integer): "))
sum_series = sum(range(1, n + 1, 2))
print("The sum of the series 1 + 3 + 5 + ... + N is:", sum_series)

# 6. Sum of Series 1 - X + X² - X³ ... ± Xⁿ
n = int(input("Enter the value of N: "))
x = int(input("Enter the value of X: "))
sum_series = 1
term = 1
for i in range(1, n + 1):
    term = -term * x
    sum_series += term
print("The sum of the series is:", sum_series)

# 7. Sum of Series 1 - 2X + 3X² - 4X³ ... ± NXⁿ⁻¹
n = int(input("Enter the value of N: "))
x = int(input("Enter the value of X: "))
sum_series = 0
for i in range(1, n + 1):
    term = i * (-x) ** (i - 1)
    sum_series += term
print("The sum of the series is:", sum_series)

# 8. GCD and LCM of Two Numbers
a = int(input("Enter the first number A: "))
b = int(input("Enter the second number B: "))

# Euclidean algorithm for GCD
while b != 0:
    a, b = b, a % b
gcd = a

# LCM calculation
lcm = (a * b) // gcd
print(f"GCD is: {gcd}")
print(f"LCM is: {lcm}")

# 9. Factorial of a Number
n = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is: {factorial}")

# 10. Divisors of a Number
n = int(input("Enter a number to find its divisors: "))
for d in range(1, n + 1):
    if n % d == 0:
        print(d)
