# Recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Function to calculate and print the factorial of a number
def print_factorial(n):
    result = factorial(n)
    print(f"The factorial of {n} is: {result}")

# Test cases
print_factorial(5)  # Expected output: The factorial of 5 is: 120 # 5 => 5 * 4 * 3 * 2 * 1 = 120
print_factorial(3)  # Expected output: The factorial of 3 is: 6
