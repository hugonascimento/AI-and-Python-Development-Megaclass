# Write a program to reverse a list and remove duplicates
# using a set

def reverse_and_remove_duplicates(input_list):
    unique_itens = set(input_list)
    reversed_list = list(unique_itens)[::-1]
    return reversed_list


input_list = input("Enter a list of items separated by spaces: ").split()
result = reverse_and_remove_duplicates(input_list)
print("\nReversed list without duplicates:", result)