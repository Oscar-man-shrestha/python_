# Q1. Write a Python program to perform addition, subtraction, multiplication, and division of two numbers.
num1 = 12 
num2 = 6  

# Addition
addition = num1 + num2
print(f"Addition of {num1} and {num2} is: {addition}")

# Subtraction
subtraction = num1 - num2
print(f"Subtraction of {num1} from {num2} is: {subtraction}")

# Multiplication
multiplication = num1 * num2
print(f"Multiplication of {num1} and {num2} is: {multiplication}")

# Division
if num2 != 0:
    division = num1 / num2
    print(f"Division of {num1} by {num2} is: {division}")
else:
    print("Division by zero is undefined.")

# Q2. Write a Python program to perform addition of three numbers.
num1 = 15  
num2 = 8   
num3 = 7   

# Addition
addition = num1 + num2 + num3
print(f"Addition of {num1}, {num2}, and {num3} is: {addition}")

# Q3. Write a Python program to calculate the area of a square given its side length.
side_length = 6  
area = side_length ** 2
print(f"Area of the square with side length {side_length} is: {area}")

# Q4. Write a Python program to calculate the area of a rectangle given its length and width.
length = 12 
width = 6    
area = length * width
print(f"Area of the rectangle with length {length} and width {width} is: {area}")

# Q5. Write a Python program to calculate the area of a circle given its radius.
radius = 10 
area = 3.14159 * radius**2
print(f"Area of the circle with radius {radius} is: {area}")

# Q6. Write a Python program to calculate the discriminant D = b² - 4ac given the values of a, b, and c.
a = 3   
b = 4   
c = 2   
D = b**2 - 4*a*c
print(f"The discriminant for the equation with a = {a}, b = {b}, and c = {c} is: {D}")

# Q7. Write a Python program to calculate √((a + b) / 2) given the values of a and b.
import math
a = 6  
b = 2  
result = math.sqrt((a + b) / 2)
print(f"The result of sqrt((a + b) / 2) for a = {a} and b = {b} is: {result}")

# Q8. Write a Python program to calculate the monthly pay of an employee given the number of hours worked in a week, the rate per hour, and the number of weeks in a month.
hours_per_week = 35  
rate_per_hour = 30  
weeks_in_month = 4  
monthly_pay = hours_per_week * rate_per_hour * weeks_in_month
print(f"The monthly pay is: Rs {monthly_pay}")

# Q9. Calculate the distance between Delhi and Mumbai, fuel cost, and journey time.
distance = 1300  
fuel_efficiency = 12  
fuel_cost_per_liter = 90  
average_speed = 85  

fuel_required = distance / fuel_efficiency
total_fuel_cost = fuel_required * fuel_cost_per_liter
journey_time = distance / average_speed

print(f"The approximate distance between Delhi and Mumbai is {distance} kilometers.")
print(f"Total fuel required: {fuel_required:.2f} liters.")
print(f"Estimated fuel cost: {total_fuel_cost:.2f}.")
print(f"Estimated journey time: {journey_time:.2f} hours.")

# Q10. Write a Python program to convert Fahrenheit to Celsius.
fahrenheit = 100  
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

# Q11. Write a Python program to convert a given integer (in seconds) to hours, minutes, and seconds.
total_seconds = 8000 
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")

# Q12. Write a Python program to calculate the speed of a vehicle.
distance = 200  
time = 4       
speed = distance / time
print(f"The speed of the vehicle is {speed} km/h.")
