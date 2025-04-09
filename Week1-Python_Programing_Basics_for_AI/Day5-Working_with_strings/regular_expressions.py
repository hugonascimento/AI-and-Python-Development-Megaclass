# Regular expressions for Pattern Matching (This is my exercise)
import re

# Regular expressions (regex) are a powerful tool for searching and manipulating strings.
# They allow you to define search patterns using a special syntax.
# Regular expressions can be used for:
# 1. Pattern matching
# 2. Searching and replacing text
# 3. Data validation
# 4. Text parsing

# Example of a simple regex pattern
# A regex pattern is a sequence of characters that defines a search pattern.
# For example, the pattern "name" will match the string "name" in a larger text.

pattern = r"name"
text = ("Hi! My name is (what?), my name is (who?), My name is (chicka, chicka) Slim Shady. (Eminem)")

# The r before the string indicates a raw string, which treats backslashes as literal characters.
# The pattern "name" will match the string "name" in the text.

# Example of using re.search() to find a pattern in a string
# The re.search() function searches the string for a match to the pattern.
# It returns a match object if a match is found, or None if no match is found.
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
    print("Match start index (first occurrence):", match.start())
    print("Match end index (first occurrence):", match.end())

    for i in range(match.start(), match.end()):
        print(f"Character at index (first occurrence) {i}: {text[i]}")
else:
    print("No match found.")

# Example of using re.findall() to find all occurrences of a pattern in a string
# The re.findall() function returns a list of all matches of the pattern in the string.
match_all = re.findall(pattern, text)
if match_all:
    count = len(match_all)
    print("Total matches found using re.findall():", count)
else:
    print("No matches found.")

# Example of using re.finditer() to find all occurrences
# The re.finditer() function returns an iterator yielding match objects for all non-overlapping matches.
# This is useful when you want to get more information about each match, such as its start and end indices.
find_matches = list(re.finditer(pattern, text))
if find_matches:
    print(f"\nTotal matches found (Using re.finditer(), list and for loop): {len(find_matches)}")
    for index, match in enumerate(find_matches):
        print(f"\nMatch {index + 1}:")
        print("Match found:", match.group())
        print("Start index:", match.start())
        print("End index:", match.end())
else:
    print("No matches found.")

# Common Functions in the re module
# 1. re.match(): Checks for a match only at the beginning of the string.
# 2. re.search(): Searches the string for a match anywhere.
# 3. re.findall(): Returns a list of all matches in the string.
# 4. re.finditer(): Returns an iterator yielding match objects for all matches.
# 5. re.sub(): Replaces occurrences of a pattern with a specified string.
# 6. re.split(): Splits the string by the occurrences of the pattern.
# 7. re.compile(): Compiles a regex pattern into a regex object for reuse.
# 8. re.escape(): Escapes all non-alphanumeric characters in a string.
# 9. re.subn(): Similar to re.sub(), but returns a tuple with the new string and the number of replacements made.
# 10. re.fullmatch(): Checks if the entire string matches the pattern.
# 11. re.purge(): Clears the cache of compiled regex patterns.
# 12. re.get_ident(): Returns the thread identifier of the current thread.
# 13. re.error: Exception raised for regex errors.
# 14. re.DEBUG: Constant used for debugging regex patterns.
# 15. re.VERBOSE: Flag that allows you to write regex patterns in a more readable format.
# 16. re.I: Flag that makes the regex case-insensitive.
# 17. re.M: Flag that allows the ^ and $ anchors to match the start and end of each line.
# 18. re.S: Flag that allows the . (dot) to match newline characters.
# 19. re.X: Flag that allows you to write regex patterns with comments and whitespace for readability.
# 20. re.A: Flag that makes the regex ASCII-only.
# 21. re.L: Flag that makes the regex locale-dependent.
# 22. re.U: Flag that makes the regex Unicode-aware.