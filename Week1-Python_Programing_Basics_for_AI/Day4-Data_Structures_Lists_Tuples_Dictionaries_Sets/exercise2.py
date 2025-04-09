# Word Frequency Counter
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize Dictionary
word_count = {}

# Count word frequence
for word in words:
    # Convert to lowercase to make the count case-insensitive
    word = word.lower()
    
    # Increment the count for the word
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print word count
#print(word_count)

# Print the word frequency
print("\nWord Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")
    
