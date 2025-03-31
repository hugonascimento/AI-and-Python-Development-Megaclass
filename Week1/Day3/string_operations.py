# A custom module string_operations.py is imported and used to perform various string operations.
# This module contains functions for string operations such as reversing a string, counting vowels, and checking for palindromes.

# reverse a string
def reverse_string(s):
    """Reverses the given string."""
    return s[::-1]

# count vowels
def count_vowels(s):
    """Counts the number of vowels in the given string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# check for palindromes
def is_palindrome(s):
    """Checks if the given string is a palindrome."""
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    return s == s[::-1]  # Check if the string is equal to its reverse
