# Sample code for Day 3: Functions, Modules, and Scope

# Importing the math module using an alias
import math as m
print("Square root using Alias", m.sqrt(16))


# Importing specific functions from a module
from math import sqrt
print("Square root using specific import:", sqrt(16))

# Importing the entire math module
import math
print("Square root using full module import:", math.sqrt(16))

# Global Scope Example
greeting = "Hi there"

def say_hello():
    # Accessing a global variable inside a function
    print(greeting + " from inside the function")

say_hello()
print(greeting + " from outside the function")

# Local Scope Example
def greet():
    # Local variable only accessible within this function
    message = "Hello World"
    print(message)

greet()
# Uncommenting the next line would cause an error because `message` is not defined globally
# print(message)

# Function with Parameters and Return Value
def add_numbers(a, b):
    # Adds two numbers and returns the result
    return a + b

result = add_numbers(45, 3)
print("Sum of 45 and 3:", result)

# General Function Syntax Example
# def function_name(parameters):
#     # code block
#     return result