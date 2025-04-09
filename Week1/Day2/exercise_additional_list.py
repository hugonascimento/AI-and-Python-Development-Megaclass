# Write a function that takes a list of numbers as input and returns the largest number in the list.
# If the list is empty, the function should return None.

# -------------------------------
# Solution 1: Static list example
# -------------------------------
# Demonstrates the function with a predefined static list.

def find_largest(numbers):
    if not numbers:  # Return None if the list is empty
        return None
    
    largest = numbers[0]  # Initialize the largest number as the first element
    index = 1  # Start checking from the second element

    while index < len(numbers):
        if numbers[index] > largest:
            largest = numbers[index]  # Update largest if a larger number is found
        index += 1  # Move to the next element

    return largest

# Example usage with a static list
numbers = [5, 3, 9, 1, 6, 7]
largest_number = find_largest(numbers)

if largest_number is not None:
    print(f"The largest number in the static list is: {largest_number}")
else:
    print("The list is empty.")

# -------------------------------
# Solution 2: User input list
# -------------------------------
# Demonstrates the function with a list of numbers provided by the user.

def find_largest(numbers):
    if not numbers:  # Return None if the list is empty
        return None
    
    largest = numbers[0]  # Initialize the largest number as the first element
    index = 1  # Start checking from the second element

    while index < len(numbers):
        if numbers[index] > largest:
            largest = numbers[index]  # Update largest if a larger number is found
        index += 1  # Move to the next element

    return largest

# Collect numbers from the user
numbers = []
for i in range(5):  # Loop to collect 5 numbers from the user
    while True:  # Repeat until a valid number is entered
        try:
            num = float(input(f"Enter number {i + 1}: "))  # Accept decimal numbers
            numbers.append(num)  # Add the number to the list
            break  # Exit the loop if input is valid
        except ValueError:  # Handle invalid input
            print("Invalid input. Please enter a valid number.")

# Find and display the largest number
largest_number = find_largest(numbers)

if largest_number is not None:
    print(f"The largest number in the list is: {largest_number}")
else:
    print("The list is empty.")