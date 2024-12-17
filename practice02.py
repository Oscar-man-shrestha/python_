# Twinkle, Twinkle, Little Star (Commented out)
# print('''
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.
# Then the trav'ller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.
# In the dark blue sky you keep,
# And often thro' my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.
# 'Tis your bright and tiny spark,
# Lights the trav'ller in the dark:
# Tho' I know not what you are,
# Twinkle, twinkle, little star.
# ''')

# p3
# Get the name and greet the user
name = input("Enter your name : ")
Name = name.title()
print(f"Good Afternoon {Name}")

# Display the current date and time
from datetime import datetime
name = input("Enter a name of participation: ")
date = datetime.now().strftime("%y-%m-%d || %H:%M:%S")
print(f"Dear {name},\n\"You Are Selected\" on: {date}")

# Handling spaces in a string
a = "oscar  man  shrestha"
detect = a.find("  ")  # Finds first occurrence of double space
findd = a.replace("  ", " ")  # Replaces double spaces with single space
print(detect)
print(findd)

# Input fruits and store them in a list
fruits = []
f1 = input('Enter a fruit 1: ')
fruits.append(f1)
f2 = input('Enter a fruit 2: ')
fruits.append(f2)
f3 = input('Enter a fruit 3: ')
fruits.append(f3)
f4 = input('Enter a fruit 4: ')
fruits.append(f4)
f5 = input('Enter a fruit 5: ')
fruits.append(f5)
f6 = input('Enter a fruit 6: ')
fruits.append(f6)
print(fruits)

# Calculate the sum of numbers in a list
number = [1, 2, 3, 4]
print(sum(number))

# Count occurrences of 0 in a tuple
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))

# Find the greatest number among four numbers
num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
num3 = int(input("Enter a number 3: "))
num4 = int(input("Enter a number 4: "))
if num1 > num2 and num1 > num3 and num1 > num4:
    print("num1 is greater")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print("num2 is greater")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print("num3 is greater")
else:
    print("num4 is greater")

# Check pass/fail based on marks
marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))
total_percentage = (((marks1 + marks2 + marks3) / 300) * 100)
if total_percentage >= 40 and total_percentage >= 33:
    print(f"YOU ARE PASS with {total_percentage:.2f}%")
else:
    print(f"FAILED {total_percentage:.2f}%")

# Message check based on specific words
c1 = "hello"
c2 = "intro plz"
c3 = "k goldai xau"
msg = input("Enter what you wanna say: ")
if c1 in msg or c2 in msg or c3 in msg:
    print("vagh nibba")
else:
    print("hajur")

# Check if "harry" is mentioned in the post
post = input("Enter a post: ")
if ("harry".lower() in post or "harry".upper() in post or "harry".capitalize() in post or "harry".title() in post):
    print("yes")
else:
    print("no")

# Print the multiplication table of a number
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")

# Print names starting with 'S' from a list
l = ["Harry", "Soham", "Sachin", "Rahul"]
for i in l:
    if "S" in i:
        print(i)

# Check if a number is prime
n = int(input("Enter a number: "))
for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

# Calculate the sum of natural numbers
n = int(input("Enter a number: "))
sum = 0
i = 0
while i <= n:
    sum += i
    i += 1
print(sum)

# Calculate the factorial of a number
n = int(input("Enter a number: "))
sum = 1
i = 1
while i < n:
    sum *= i
    i += 1
print(sum)

# Print a star pattern
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1), end="")
    print()

# Print a rectangle pattern
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print("*" * n)
    print("*" + " " * (n - 2) + "*")
    print("*" * n)

# Reverse multiplication table
n = int(input("Enter a number: "))
for i in reversed(range(1, 11)):
    print(f"{n} x {i} = {n*i}")

# Looping and skipping numbers
for i in range(4):
    print("printing")
    if i == 2:
        continue
    print(i)

# Print a rectangle pattern with function
def rectangle(width, height):
    for i in range(height):
        print("*" * width)
rectangle(5, 3)

# Print a square pattern with function
def square(length):
    for i in range(length):
        print("*" * length, end="")
    print()
square(5)

# Print a rhombus pattern
def rhombus(N):
    for i in range(1, N + 1):
        print(" " * (N - i) + "*" * N)
    print()
rhombus(5)

# Print a simple number pattern
width = 4
height = 5
for i in range(height):
    for num in range(1, width + 1):
        print(num, end="")
    print()

# Print a number pattern
breadth = int(input("Enter breadth: "))
length = int(input("Enter length: "))
for i in range(1, length + 1):
    for j in range(1, breadth + 1):
        print(j, end="")
    print()

# Print a pyramid pattern
N = int(input("Enter a number: "))
for i in range(1, N + 1):
    print(" " * (N - i), end="")
    for j in range(1, N + 1):
        print(j, end="")
    print()

# Nested pattern printing
N = int(input("Enter a number: "))
for i in range(1, N + 1):
    print(" " * (N - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Final star pattern
N = int(input("Enter a number: "))
for i in range(1, N + 1):
    print(" " * (N - i), end="")
    for j in range(1, 2 * i):
        print(i, end="")
    print()
