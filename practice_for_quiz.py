def factorial(n):
    if (n == 0 or n == 1):
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
    if (n == 1 or n == 0):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

def sum(n):
    if n == 0 or n == 1:
        return n
    return n + sum(n - 1)

print(sum(3))

def palindrome(s):
    if len(s) <= 0:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

print(palindrome("naman"))

def power(x, y):
    if (y == 0):
        return 1
    return x * power(x, y - 1)

print(power(2, 3))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))

def dtob(n):
    if n == 0:
        return ""
    return dtob(n // 2) + str(n % 2)

print(dtob(10))

def reverse(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse(s[:-1])

print(reverse("oscar"))

def sum(n):
    if n == 0:
        return 0
    return n % 10 + sum(n // 10)

print(sum(123))

def product_of_array(arr, n):
    if (n == 0):
        return arr[0]
    return arr[n] * product_of_array(arr, (n - 1))

print(product_of_array([1, 2, 3, 4], 3))

def sorted(arr, n):
    if n == 1:
        return True
    return arr[n - 1] >= arr[n - 2] and sorted(arr, n - 1)

print(sorted([1, 2, 3, 4], 3))

def subsets(s):
    if len(s) == 0:
        return [[]]
    smaller_subsets = subsets(s[1:])
    return smaller_subsets + [[s[0]] + ss for ss in smaller_subsets]

print(subsets([1, 2, 3]))

def tower_of_hanoi(n, start, aux, end):
    if (n == 1):
        print(f"Move disk 1 from tower {start} to tower {end}")
        return
    tower_of_hanoi(n - 1, start, end, aux)
    print(f"Move disk {n} from tower {start} to {end}")
    tower_of_hanoi(n - 1, aux, start, end)

tower_of_hanoi(3, "A", "B", "C")

def count_ways(n):
    if n <= 1:
        return 1
    return count_ways(n - 1) + count_ways(n - 2)

print(count_ways(4))

def permutations(s, chosen=""):
    if len(s) == 0:
        print(chosen)
    else:
        for i in range(len(s)):
            c = s[i]
            remaining = s[:i] + s[i + 1:]
            permutations(remaining, chosen + c)

permutations("oscar")
