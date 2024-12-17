# Traffic light system using switch-case style in Python (match-case)
def traffic(color):
    match color:
        case 'red':
            return 'STOP'
        case 'YELLOW':
            return 'GET READY'
        case 'green':
            return 'GO'
        case _:
            return "INVALID"

print(traffic("green"))

# Function that performs different operations based on the input
def function(operation, a, b):
    match operation:
        case "sum":
            return a + b
        case "sub":
            return a - b
        case "divide":
            if b != 0:
                return a / b
            else:
                return "Cannot divide by zero"
        case _:
            return "INVALID"

result = function("sum", 1, 5)
print(result)
