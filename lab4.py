# 1. Check Whether the Number is Positive or Negative
def check_number(number):
    if number > 0:
        return "Positive"
    if number < 0:
        return "Negative"

number = float(input("Enter a number: "))
result = check_number(number)
if result:
    print(f"The number is {result}.")

# 2. Check Whether the Number is Positive, Negative, or Zero
def check_number(number):
    if number > 0:
        return "Positive"
    if number < 0:
        return "Negative"
    return "Zero"

number = float(input("Enter a number: "))
result = check_number(number)
print(f"The number is {result}.")

# 3. Check Whether the Number is Odd or Even
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

number = int(input("Enter a number: "))
result = check_odd_even(number)
print(f"The number is {result}.")

# 4. Check Whether a Person is Eligible for Voting
def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible to vote"
    return "Not eligible to vote"

age = int(input("Enter your age: "))
result = check_voting_eligibility(age)
print(f"You are {result}.")

# 5. Largest Among Three Numbers
a = 32
b = 27
c = 25

largest = a if (a > b and a > c) else (b if b > c else c)
print("The largest number is:", largest)

# 6. Grade Based on Average Marks
avg_marks = float(input("Enter your average marks: "))
if avg_marks > 80:
    grade = "A"
elif avg_marks > 60 and avg_marks <= 80:
    grade = "B"
elif avg_marks > 40 and avg_marks <= 60:
    grade = "C"
else:
    grade = "F"
print(f"Your grade is: {grade}")

# 7. Game Points Based on User Input (Vowel, Number, or Other)
char = input("Enter a character: ")

if char.isdigit():
    points = 10
elif char.lower() in 'aeiou':
    points = 5
else:
    points = 0

print(f"Points scored: {points}")

# 8. Check Whether a Character is Uppercase or Lowercase
char = input("Enter a character: ")

if char.isalpha():  # Check if the character is a letter
    if char.islower():
        print("You entered a lowercase letter.")
    elif char.isupper():
        print("You entered an uppercase letter.")
else:
    print("The input is not a letter.")

# 9. Game to Determine the Nature of Roots of a Quadratic Equation
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    points = 20
    root_type = "real and distinct roots"
elif discriminant == 0:
    points = 0
    root_type = "equal roots"
else:
    points = 10
    root_type = "imaginary roots"

print(f"Discriminant: {discriminant}")
print(f"Nature of roots: {root_type}")
print(f"Points awarded: {points}")

# 10. Classify a Person Based on BMI
weight = float(input("Enter weight (in kg): "))
height = float(input("Enter height (in meters): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    classification = "Underweight"
elif 18.5 <= bmi < 25:
    classification = "Normal Weight"
else:
    classification = "Overweight"

print(f"BMI: {bmi:.2f}")
print(f"Classification: {classification}")

# 11. Find the Quadrant Based on X and Y Coordinates
x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x > 0 and y > 0:
    quadrant = "Quadrant I"
elif x < 0 and y > 0:
    quadrant = "Quadrant II"
elif x < 0 and y < 0:
    quadrant = "Quadrant III"
elif x > 0 and y < 0:
    quadrant = "Quadrant IV"
elif x == 0 and y != 0:
    quadrant = "On the Y-axis"
elif x != 0 and y == 0:
    quadrant = "On the X-axis"
else:
    quadrant = "Origin"

print(f"The point ({x}, {y}) is in {quadrant}.")
