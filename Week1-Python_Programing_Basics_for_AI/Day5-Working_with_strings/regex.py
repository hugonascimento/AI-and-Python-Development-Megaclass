import re
text = "Contact me at 123-456-7890"

# Find all occurrences of digits in the text
digits = re.findall(r'\d+', text)
print("Digits found:", digits)  # Output: Digits found: ['123', '456', '7890']

# Replace all digits with 'X'
updated_text = re.sub(r'\d+', 'X', text)
print("Updated text:", updated_text)  # Output: Updated text: Contact me at X-X-X

