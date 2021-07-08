
def alphasort(string):
    words = string.split()

    unique_words = set(words)
    sorted_words = sorted(unique_words, key=str.lower)

    output = " ".join(sorted_words)

    return output
