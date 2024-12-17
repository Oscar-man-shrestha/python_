# 1. Factorial of a Number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# 2. Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8

# 3. Sum of Natural Numbers
def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

print(sum_natural(5))  # Output: 15

# 4. Check if a String is a Palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))  # Output: True

# 5. Power of a Number (x^y)
def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y - 1)

print(power(2, 3))  # Output: 8

# 6. Greatest Common Divisor (GCD) using Euclidean Algorithm
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))  # Output: 6

# 7. Decimal to Binary Conversion
def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

print(decimal_to_binary(10))  # Output: 1010

# 8. Reverse a String
def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # Output: olleh

# 9. Sum of Digits of a Number
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))  # Output: 6

# 10. Product of Array Elements
def product_of_array(arr, n):
    if n == 0:
        return arr[0]
    return arr[n] * product_of_array(arr, n - 1)

print(product_of_array([1, 2, 3, 4], 3))  # Output: 24

# 11. Check if an Array is Sorted
def is_sorted(arr, n):
    if n == 1:
        return True
    return arr[n - 1] >= arr[n - 2] and is_sorted(arr, n - 1)

print(is_sorted([1, 2, 3, 4], 4))  # Output: True

# 12. Generate All Subsets of a Set
def subsets(s):
    if len(s) == 0:
        return [[]]
    smaller_subsets = subsets(s[1:])
    return smaller_subsets + [[s[0]] + ss for ss in smaller_subsets]

print(subsets([1, 2, 3]))  # Output: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

# 13. Tower of Hanoi
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

tower_of_hanoi(3, 'A', 'C', 'B')

# 14. Count Ways to Climb Stairs (1 or 2 Steps at a Time)
def count_ways(n):
    if n <= 1:
        return 1
    return count_ways(n - 1) + count_ways(n - 2)

print(count_ways(4))  # Output: 5

# 15. Permutations of a String
def permutations(s, chosen=""):
    if len(s) == 0:
        print(chosen)
    else:
        for i in range(len(s)):
            c = s[i]
            remaining = s[:i] + s[i + 1:]
            permutations(remaining, chosen + c)

permutations("abc")  # Output: All permutations of "abc"

# 16. Find All Possible Combinations of k Elements from a List
def combinations(arr, k):
    if k == 0:
        return [[]]
    if len(arr) < k:
        return []
    with_first = [[arr[0]] + comb for comb in combinations(arr[1:], k - 1)]
    without_first = combinations(arr[1:], k)
    return with_first + without_first

print(combinations([1, 2, 3, 4], 2))  # Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

# 17. Calculate the nth Triangular Number
def triangular_number(n):
    if n == 1:
        return 1
    return n + triangular_number(n - 1)

print(triangular_number(5))  # Output: 15

# 18. Sum of a List of Numbers
def list_sum(lst):
    if not lst:
        return 0
    return lst[0] + list_sum(lst[1:])

print(list_sum([1, 2, 3, 4]))  # Output: 10

# 19. Calculate the Binomial Coefficient (n choose k)
def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

print(binomial_coefficient(5, 2))  # Output: 10

# 20. Generate All Permutations of a List
def permute(arr):
    if len(arr) == 0:
        return [[]]
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i + 1:]
        for perm in permute(rest):
            result.append([arr[i]] + perm)
    return result

print(permute([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
