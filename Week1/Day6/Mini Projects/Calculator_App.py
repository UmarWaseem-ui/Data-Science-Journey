# Features:
    # Addition
    # Subtraction
    # Multiplication
    # Division

def calculator(a,b,operation):
    if(operation == "sum"):
        return a+b
    elif(operation == "subtract"):
        return a-b
    elif(operation == "multiply"):
        return a*b
    elif(operation == "divide"):
        if (b == 0):
            return "Error"
        else:
            return a/b
        
print(calculator(2,4,"sum"))
print(calculator(4,2,"subtract"))
print(calculator(2,2,"multiply"))
print(calculator(4,0,"divide"))    