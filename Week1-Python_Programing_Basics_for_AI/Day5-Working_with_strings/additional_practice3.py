# Write a program to reverse the words in a sentence (not the letters)
# Example: "Hello World" -> "World Hello"
import re

def reverse_words(sentence):
    # Split the sentence into words and punctuation
    words = re.findall(r'\b\w+\b|[.,!?;]', sentence)
    # Extract punctuation if it exists at the end
    punctuation = ''
    if words and re.match(r'[.,!?;]', words[-1]):
        punctuation = words.pop()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed words back into a string and append the punctuation
    return ' '.join(reversed_words) + punctuation

print(f"The reversed sentence is: {reverse_words(input('Enter a sentence to reverse the words: '))}")
