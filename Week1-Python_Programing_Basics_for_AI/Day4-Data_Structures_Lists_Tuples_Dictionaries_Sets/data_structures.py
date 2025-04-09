# Lists

numbers = [1, 2, 3, 4, 5]

fruits = ["apple", "banana", "cherry"]

mixed = [1, "apple", True]

# List indexing
print(numbers[2])  # Prints the third element of the numbers list: 3
print(fruits[1])  # Prints the second element of the fruits list: banana
print(mixed[0])  # Prints the first element of the mixed list: 1
print(mixed[1])  # Prints the second element of the mixed list: apple
print(mixed[2])  # Prints the third element of the mixed list: True
print(fruits[-1])  # Prints the last element of the fruits list: cherry

# List slicing
print(numbers[1:3])  # Prints a slice of numbers from index 1 to 2: [2, 3]
print(fruits[0:2])  # Prints a slice of fruits from index 0 to 1: ['apple', 'banana']
print(mixed[0:2])  # Prints a slice of mixed from index 0 to 1: [1, 'apple']
print(numbers[:3])  # Prints the first three elements of numbers: [1, 2, 3]

# List comprehension
squared_numbers = [x**2 for x in numbers]  # Create a new list with squared numbers
print(squared_numbers)  # Prints the list of squared numbers: [1, 4, 9, 16, 25]

# List methods
print(fruits)  # Prints the original fruits list: ['apple', 'banana', 'cherry']
fruits.remove("banana")  # Remove 'banana' from the list
print(fruits)  # Prints the updated fruits list: ['apple', 'cherry']
fruits.append("orange")  # Add 'orange' to the end of the list
print(fruits)  # Prints the updated fruits list: ['apple', 'cherry', 'orange']
fruits.insert(1, "kiwi")  # Insert 'kiwi' at index 1
print(fruits)  # Prints the updated fruits list: ['apple', 'kiwi', 'cherry', 'orange']

fruits.__delitem__(2)  # Delete the item at index 2 (not commonly used; prefer 'del fruits[2]')
print(fruits)  # Prints the updated fruits list: ['apple', 'kiwi', 'orange']

fruits.append("banana")  # Add 'banana' to the end of the list
print(fruits)  # Prints the updated fruits list: ['apple', 'kiwi', 'orange', 'banana']
del fruits[0]  # Delete the item at index 0
print(fruits)  # Prints the updated fruits list: ['kiwi', 'orange', 'banana']

# List concatenation
fruits += ["grape", "pear"]  # Add 'grape' and 'pear' to the list
print(fruits)  # Prints the updated fruits list: ['kiwi', 'orange', 'banana', 'grape', 'pear']

# Save a copy of the list before repetition
fruits_original = fruits.copy()  # Create a copy of the current state of the list

# List repetition
fruits *= 2  # Repeat the list
print(fruits)  # Prints the repeated fruits list: ['kiwi', 'orange', 'banana', 'grape', 'pear', 'kiwi', 'orange', 'banana', 'grape', 'pear']

# Restore the original state of the list
fruits = fruits_original  # Restore the list to its original state
print(fruits)  # Prints the restored fruits list: ['kiwi', 'orange', 'banana', 'grape', 'pear']

# List sorting
fruits.sort()  # Sort the list in ascending order
print(fruits)  # Prints the sorted fruits list: ['banana', 'grape', 'kiwi', 'orange', 'pear']

# List reversing
fruits.reverse()  # Reverse the list
print(fruits)  # Prints the reversed fruits list: ['pear', 'orange', 'kiwi', 'grape', 'banana']

# List length
print(len(fruits))  # Prints the length of the fruits list: 5

# List membership
print("apple" in fruits)  # Prints False because 'apple' is not in the fruits list
print("banana" in fruits)  # Prints True because 'banana' is in the fruits list

# List copying
fruits_copy = fruits.copy()  # Create a shallow copy of the list

# List clearing
fruits.clear()  # Remove all items from the list
print(fruits)  # Prints the cleared fruits list: []

fruits = fruits_copy  # Restore the original state of the list
print(fruits)  # Prints the restored fruits list: ['pear', 'orange', 'kiwi', 'grape', 'banana']

sliced_fruits = fruits[1:3]  # Create a slice of the list
print(sliced_fruits)  # Prints the sliced fruits list: ['orange', 'kiwi']

# Tuple
# Tuples are immutable

colors = ("red", "green", "blue")
# single_item = ("glass",)  # Tuple with a single item (note the comma)
single_item = ("glass",)  # This is a tuple with one item.
not_a_tuple = "glass"  # This is just a string inside parentheses, not a tuple.

# Tuple indexing
print(colors)  # Prints the entire colors tuple: ('red', 'green', 'blue')
print(colors[0])  # Prints the first element of the colors tuple: red
print(colors[-1])  # Prints the last element of the colors tuple: blue
print(single_item)  # Prints the single item tuple: ('glass',)

# Dictionaries
# Dictionaries are unordered collections of key-value pairs
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
}
print(person)  # Prints the entire person dictionary: {'name': 'John', 'age': 30, 'city': 'New York'}
print(person["name"])  # Prints the value associated with the key 'name': John

person["age"] = 42  # Update the value associated with the key 'age'
print(person)  # Prints the updated person dictionary: {'name': 'John', 'age': 42, 'city': 'New York'}
print(person.get("city"))  # Prints the value associated with the key 'city': New York

student = {
    "name": "Alice",
    "age": 25,
    "grade": "A",
    "courses": ["Math", "Science"],
}
print(student)  # Prints the entire student dictionary: {'name': 'Alice', 'age': 25, 'grade': 'A', 'courses': ['Math', 'Science']}
print(student["courses"][1])  # Prints the second element of the courses list: Science

student["courses"].append("History")  # Add 'History' to the courses list
student["subjects"] = ["Math", "Science", "History"]  # Add a new key-value pair

print(student)  # Prints the updated student dictionary: {'name': 'Alice', 'age': 25, 'grade': 'A', 'courses': ['Math', 'Science', 'History'], 'subjects': ['Math', 'Science', 'History']}

student["age"] = 42  # Update the value associated with the key 'age'
print(student)  # Prints the updated student dictionary: {'name': 'Alice', 'age': 42, 'grade': 'A', 'courses': ['Math', 'Science', 'History'], 'subjects': ['Math', 'Science', 'History']}

del student["grade"]  # Delete the key-value pair with key 'grade'
# Does not return anything.
# Raises an error (KeyError) if the key does not exist.

print(student)  # Prints the updated student dictionary: {'name': 'Alice', 'age': 42, 'courses': ['Math', 'Science', 'History'], 'subjects': ['Math', 'Science', 'History']}

student.pop("subjects")  # Remove the key-value pair with key 'subjects'
# Returns the value associated with the removed key.
# Allows specifying a default value to return if the key does not exist, avoiding an error.
# grade = student.pop("grade")  # Returns the value associated with the key "grade"
# grade = student.pop("grade", None)  # Returns None if the key does not exist

print(student)  # Prints the updated student dictionary: {'name': 'Alice', 'age': 42, 'courses': ['Math', 'Science', 'History']}

for key, value in student.items():
    print(key, value)  # Prints each key-value pair in the student dictionary
    
# Sets
# Sets are unordered collections of unique elements
numbers = {1, 2, 3, 4}

empty_set = set()  # Create an empty set

print(numbers)  # Prints the entire numbers set: {1, 2, 3, 4}
numbers.add(5)  # Add an element to the set
print(numbers)  # Prints the updated numbers set: {1, 2, 3, 4, 5}
numbers.remove(3)  # Remove an element from the set
print(numbers)  # Prints the updated numbers set: {1, 2, 4, 5}
numbers.discard(2)  # Remove an element from the set (no error if not found)
print(numbers)  # Prints the updated numbers set: {1, 4, 5}
numbers.discard(10)  # Try to remove an element not in the set (no error)
print(numbers)  # Prints the updated numbers set: {1, 4, 5}
numbers.clear()  # Remove all elements from the set
print(numbers)  # Prints the cleared numbers set: set()


set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))  # Prints the union of set1 and set2: {1, 2, 3, 4, 5}
print(set1 | set2)  # Prints the union of set1 and set2: {1, 2, 3, 4, 5}

print(set1.intersection(set2))  # Prints the intersection of set1 and set2: {3}
print(set1 & set2)  # Prints the intersection of set1 and set2: {3}

print(set1 - set2)  # Prints the difference of set1 and set2: {1, 2}
print(set1.difference(set2))  # Prints the difference of set1 and set2: {1, 2}

print(set1 ^ set2)  # Prints the symmetric difference of set1 and set2: {1, 2, 4, 5}
print(set1.symmetric_difference(set2))  # Prints the symmetric difference of set1 and set2: {1, 2, 4, 5}

print(set1.issubset(set2))  # Prints False because set1 is not a subset of set2
print(set1 <= set2)  # Prints False because set1 is not a subset of set2

print(set1.issuperset(set2))  # Prints False because set1 is not a superset of set2
print(set1 >= set2)  # Prints False because set1 is not a superset of set2

print(set1.isdisjoint(set2))  # Prints False because set1 and set2 have common elements

