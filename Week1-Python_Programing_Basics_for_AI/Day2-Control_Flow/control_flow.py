# Example 1: Checking a condition
print("Example 1: Checking a condition")

num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Example 2: Nested conditions
print("\nExample 2: Nested conditions")
age = 25
if age > 18:
    if age < 30:
        print("Young Adult")
    else:
        print("Adult")

# Syntax for a for loop
# for item in sequence:
    # do something with item

# Loop through a list
print("\nExample 3: Loop through a list")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with range
print("\nExample 4: Loop with range")
for i in range(5):  # [0, 1, 2, 3, 4]
    print(i)

# Syntax for a while loop
# while TRUE condition:
    # do something

# Example 5: While loop
print("\nExample 5: While loop")
count = 5
while count > 0:
    print(count)
    count -= 1  # stop the loop
print("Outside while loop")

# Example 6: Break statement
print("\nExample 6: Break statement")
for i in range(10):
    if i == 5:
        break
    print(i)
print("Outside for loop")

# Example 7: Continue statement
print("\nExample 7: Continue statement")
for i in range(10):
    if i == 5:
        continue
    print(i)
print("Outside for loop")

# Example 8: Skip even numbers
print("\nExample 8: Skip even numbers")
for i in range(10):
    # Skip even numbers
    if i % 2 == 0:
        continue
    print(i)

