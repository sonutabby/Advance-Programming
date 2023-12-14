#Function definitions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero!"

def modulus(x, y):
    return x % y

def check_greater(x, y):
    return x > y

#Displaying the calculator menu
print("Calculator Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Check greater number")

while True:
    #User input for operation choice
    choice = input("Enter choice (1-6) or 'Q' to quit: ")

    if choice.upper() == 'Q':
        break

    try:
        choice = int(choice)
        if choice < 1 or choice > 6:
            print("Invalid choice! Please enter a number from 1 to 6.")
            continue

        #Getting user input for numbers
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        #Performing the selected operation
        if choice == 1:
            result = add(x, y)
        elif choice == 2:
            result = subtract(x, y)
        elif choice == 3:
            result = multiply(x, y)
        elif choice == 4:
            result = divide(x, y)
        elif choice == 5:
            result = modulus(x, y)
        elif choice == 6:
            result = check_greater(x, y)

        #Displaying the result
        print(f"Result: {result}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")