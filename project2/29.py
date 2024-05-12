def get_unique_words(filename):
    """Read a file and return a set of unique words."""
    unique_words = set()
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                
                word = word.strip(",.?!;:")
                unique_words.add(word)
    return unique_words


filename = input("Enter the name of the text file: ")


unique_words = get_unique_words(filename)


print("Unique words in the file:")
for word in unique_words:
    print(word)

