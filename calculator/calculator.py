import math

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Division by zero is not possible"
    return num1 / num2

def modulus(num1, num2):
    return num1 % num2

def exponent(num1, num2):  
    return num1 ** num2

def sqrt(num):
    if num < 0:
        return "Error!"
    return math.sqrt(num)

def log(num):
    if num <= 0:
        return "Error!"
    return math.log(num)

def calculator():
    operation = input("\nEnter operation (+, -, *, /, %, **, sqrt, log): ")

    if operation in ["+", "-", "*", "/", "%", "**"]:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if operation == "+":
            print("Addition is:", add(num1, num2))
        elif operation == "-":
            print("Subtraction is:", sub(num1, num2))
        elif operation == "*":
            print("Multiplication is:", mul(num1, num2))
        elif operation == "/":
            print("Division is:", div(num1, num2))
        elif operation == "%":
            print("Modulus is:", modulus(num1, num2))
        elif operation == "**":
            print("Exponentiation is:", exponent(num1, num2))

    elif operation in ["sqrt", "log"]:
        num = int(input("Enter a number: "))
        
        if operation == "sqrt":
            print("Square Root is:", sqrt(num))
        elif operation == "log":
            print("Log of a number is:", log(num))

    else:
        print("Invalid operation! Please try again.")

    choice = input("\nDo you want to continue? (y/n): ")
    if choice == "y":
        calculator()  
    else:
        print("Goodbye!")  

calculator()
