# Write a program to count number of vowels in a string

import re

def count_vowels(text):
    # Regex pattern to match vowels, including accented vowels
    vowel_pattern = r'[aeiouAEIOUáéíóúãõâêîôû]'
    # Find all occurrences of the pattern
    vowels = re.findall(vowel_pattern, text)
    # Return the count of vowels
    return len(vowels)

# text = input("Enter a string: ")
# vowel_count = count_vowels(text)
# print(f"The number of vowels in the string is: {vowel_count}")

# Combine the two functions into one
print(f"The number of vowels in the string is: {count_vowels(input('Enter a string: '))}")