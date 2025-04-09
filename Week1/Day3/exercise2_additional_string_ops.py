# Exercise 2: Create a module for string operations, including functions to reverse a string, count vowels, and check for palindromes. 
# Import into a script and test the functions.

import string_operations as so
# This script imports the string_operations module and provides 
# a menu-driven interface

while True:
    # Display the menu of string operations
    print("\nMenu:")
    print("1. Reverse a string")
    print("2. Count vowels in a string")
    print("3. Check if a string is a palindrome")
    print("0. Exit")
    
    # Get the user's choice
    choice = input("\nEnter your choice: ")
    
    # Exit the program if the user chooses option 0
    if choice == '0':
        print("\nExiting the program.")
        break
    
    # Handle valid choices for string operations
    elif choice in ['1', '2', '3']:
        # Get a string from the user
        user_string = input("\nEnter a string: ")
        
        # Perform the chosen operation and display the result
        if choice == '1':
            print(f"\nReversed string: {so.reverse_string(user_string)}")
        
        elif choice == '2':
            print(f"\nNumber of vowels: {so.count_vowels(user_string)}")
            
        elif choice == '3':
            if so.is_palindrome(user_string):
                print("\nThe string is a palindrome.")
            else:
                print("\nThe string is not a palindrome.")
    # Handle invalid menu choices
    else:
        print("\nInvalid choice. Please try again.")
        
