# Working with strings

# Concatenation
first = "Hello"
second = "World"
# Concatenation
result = first + " " + second
print(result)  # Output: Hello World

# Slicing
text = "Python Programming"
print(text[0:6])  # Output: Python
print(text[7:])  # Output: Programming
print(text[-11:])  # Output: Programming

# Formatting
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 25 years old.

# Common string methods
# split()
# join()
# replace()
# strip()

# Example of split()
text1 = "Python,is,fun"
# When you use split(","), you are telling Python to split the string whenever it encounters a comma (,)
split_with_comma = text1.split(",")
print(split_with_comma)  # Output: ['Python', 'is', 'fun']

text2 = "Python is fun"
# When you use split(" "), you are telling Python to split the string whenever it encounters whitespace.
split_with_witespace = text2.split(" ")
print(split_with_witespace)  # Output: ['Python', 'is', 'fun']


# Example of join()
my_list = ['Python', 'is', 'fun']
join1 = " ".join(my_list)
print(join1)  # Output: Python is fun

# Example of replace()
text3 = 'Python is fun'
find_and_replace = text3.replace("is", "is not")
print(find_and_replace)  # Output: Python is not fun

# Example of replace() with no match
text4 = 'Python is cool'
no_replace = text4.replace("Java", "is not")
print(no_replace)  # Output: Python is cool (no change, as "Java" is not in the string)

# Example of replace() with empty string
text5 = 'Python is great'
replace_and_remove_spaces = text5.replace(" ", "")
print(replace_and_remove_spaces)  # Output: Pythonisgreat (all spaces removed)

# Example of strip()
text6 = "   Python is easy   "
strip_witespace = text6.strip()
print(strip_witespace)  # Output: Python is easy

