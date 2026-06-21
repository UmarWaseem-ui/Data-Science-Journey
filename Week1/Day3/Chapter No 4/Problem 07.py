# Addition Function
def add(a,b):
     sum=a+b
     return sum

print(add(2,4))

# Calculator
def cal(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b
    else:
        return "Invalid operation"

# Testing the calculator
print(cal(2, 4, "add"))      
print(cal(2, 4, "multiply"))