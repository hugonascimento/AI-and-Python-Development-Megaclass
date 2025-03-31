# Exercise 1: Write a function to check if a number is even or odd
# and call it within another function.

# Function to determine if a number is even or odd
def is_even_or_odd(n):
    # Check if the number is divisible by 2
    if n % 2 == 0:
        return "Even"  # Return "Even" if divisible by 2
    else:
        return "Odd"  # Return "Odd" otherwise

# Function to check a number and print whether it is even or odd
def check_number(n):
    # Call the is_even_or_odd function and store the result
    result = is_even_or_odd(n)
    # Print the result
    print(f"The number {n} is: {result}")

# Infinite loop to continuously ask the user for input
while True:
    try:
        # Prompt the user to enter a number or type 'exit' to quit
        choice = input(
            "Enter a number to check if it's even or odd (or type 'exit' to quit): "
        )
        # Check if the user wants to exit the program
        if choice.lower() == "exit":  
            print("Exiting the program.")  # Print exit message
            break  # Exit the loop
        else:
            # Convert the input to an integer
            number = int(choice) 
            # Call the check_number function with the input number
            check_number(number)
    except ValueError:
        # Handle invalid input (non-integer values)
        print("Invalid input. Please enter a valid integer.")
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("\nExiting the program.")
        break
