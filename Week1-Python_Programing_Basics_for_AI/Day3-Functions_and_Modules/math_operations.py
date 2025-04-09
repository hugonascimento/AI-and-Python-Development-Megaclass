# A custom module math_operations.py is imported and used to perform basic arithmetic operations.

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract the second number from the first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide the first number by the second
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"
