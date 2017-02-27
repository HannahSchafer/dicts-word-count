import sys

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

        punctuation = [",", ".", "!", "?", ":", ";", "/", "(", ")", "{", "}", "[",
                       "]", "|", "*", "&", "#", "$", "^"]
        # Iterating over the words to add into the dictionary
        for word in words:
            word = word.lower()
            if word[-1] in punctuation:
                word = word[:-1]
            word_counts[word] = word_counts.get(word, 0) + 1

    text.close()
    return word_counts


def print_dict(file_name):
    """Calling the count_words function and printing each word and its count.
    """

    dictionary = count_words(file_name)

    # Breaking dictionary into tuples, and printing out each key and its value
    for word, count in dictionary.iteritems():
        print "{}: {}".format(word, count)

print_dict(sys.argv[1])

