# Exercise 2: Check is a String is a Palindrome
# Palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum()) # Filter out non-alphanumeric characters
    return text == text[::-1] # Check if the cleaned text is the same forwards and backwards

input_text = input("Enter a string: ")
if is_palindrome(input_text):
    print(f'"{input_text}" is a palindrome.')
else:
    print(f'"{input_text}" is not a palindrome.')
    
# Examples: 
# "A man, A plan, a canal, Panama".
# "Ana, Ovo, Osso, Radar, Renner, Arara, Reviver, Somávamos"
