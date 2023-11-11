# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main program
while True:
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter 'x' for multiplication")
    print("Enter '/' for division")
    print("Enter 'Quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ["+", "-", "x", "/"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "+":
            result = add(num1, num2)
        elif user_input == "-":
            result = subtract(num1, num2)
        elif user_input == "x":
            result = multiply(num1, num2)
        elif user_input == "/":
            result = divide(num1, num2)
        
        print("Result: " + str(result))
    else:
        print("Invalid input. Please enter a valid operation.")

