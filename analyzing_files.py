def count_words(fileName):
    """Count the approimate number of words in a file."""
    try:
        with open(fileName) as file:
            contents = file.read()
    except FileNotFoundError:
        with open("learning_python.txt", 'a') as file_:
            file_.write('\n' + fileName)
        pass # This line allows python to do nothing when this error is encountered
        # print("Sorry, the file " + fileName + " does not exist.")
    else:
        # The split() method separates a string into parts wherever it finds a
        # space and stores all the parts of the string in a list.
        words = contents.split()
        len_words = len(words)
        print("The file " + fileName + " has about " + str(len_words) + " words.")

fileNames = ['pi_digits.txt', 'file__.txt']
for files in fileNames:
    count_words(files)