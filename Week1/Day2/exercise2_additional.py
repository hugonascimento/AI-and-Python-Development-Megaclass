# This program is a simple calculator that can perform addition, subtraction, multiplication, division, and factorial calculations.
# The user can choose an operation, input numbers, and see the result. The program runs until the user chooses to exit.

# Define a function to add two numbers
def sum(a, b):
    return a + b

# Define a function to subtract the second number from the first
def subtract(a, b):
    return a - b

# Define a function to multiply two numbers
def multiply(a, b):
    return a * b

# Define a function to divide the first number by the second
# Returns an error message if division by zero is attempted
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

# Define a function to calculate the factorial of a number
# Returns an error message if the number is negative
def factorial(n):
    if n < 0:
        return "Error: Factorial of a negative number is not defined."
    result = 1
    counter = 1 # Only used for the while loop
    
    while counter <= n:
        result *= counter
        counter += 1
    
    # Alternative implementation using a for loop    
    #for i in range(1, int(n) + 1):
    #    result *= i
    
    return result

# Define a function to get a valid number from the user
# Keeps prompting until the user enters a valid float
def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))  # Convert input to float
        except ValueError:
            print("Invalid input. Please enter a valid number.")  # Handle invalid input

# Main program loop
while True:
    # Display the menu of operations
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Factorial")
    print("0. Exit")
    
    # Get the user's choice
    choice = input("Enter your choice: ")
    
    # Exit the program if the user chooses option 0
    if choice == '0':
        print("Exiting the program.")
        break
    
    # Handle valid choices for mathematical operations
    elif choice in ['1', '2', '3', '4']:
        # Get two valid numbers from the user
        num1 = get_valid_number("Enter first number: ")
        num2 = get_valid_number("Enter second number: ")
        
        # Perform the chosen operation and display the result
        if choice == '1':
            print(f"Result: {sum(num1, num2)}")
        
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
            
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        
    # Handle valid choice for factorial
    elif choice == '5':
        # Get a valid non-negative integer from the user
        num = get_valid_number("Enter a non-negative integer: ")
        if num.is_integer() and num >= 0:
            print(f"Result: {factorial(num)}")
        else:
            print("Error: Please enter a non-negative integer.")
    
    # Handle invalid menu choices
    else:
        print("Invalid input. Please try again.")
