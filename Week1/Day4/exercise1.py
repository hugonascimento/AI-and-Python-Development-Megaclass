# Manipulate Data in a Dictionary
person = {"name": "Alice", "age": 25, "grade": "A"}

# Add new key-value pairs
person["address"] = "123 Main St"

# Update Age
person["age"] = 32

# Remove grade
if "grade" in person:
    del person["grade"]

print(person)  # Prints the updated person dictionary: {'name': 'Alice', 'age': 32, 'address': '123 Main St'}