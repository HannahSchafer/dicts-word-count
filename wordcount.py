# put your code here.
def count_words(file_name):
    """Counts the number of times a word is used in a text file.
    """

    # Create empty dictionary
    word_counts = {}
    text = open(file_name)

    # Iterating over the text to split into lines and unique words
    for line in text:
        line = line.rstrip()
        words = line.split(" ")

        # Iterating over the words to add into the dictionary
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    text.close()
    return word_counts

print count_words("test.txt")

print count_words("twain.txt")
