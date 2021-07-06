words = input("Put some words in! ").split()

unique_words = set(words)
sorted_words = sorted(unique_words, key=str.lower)

output = " ".join(sorted_words)

print(output)
