fileName = input("""Enter the name a file present 
in this folder with it's extension: """)

try:
    with open(fileName) as file:
        contents = file.read()
except FileNotFoundError:
    print("Sorry, the file " + fileName + " does not exist.")
else:
    # The split() method separates a string into parts wherever it finds a
    # space and stores all the parts of the string in a list.
    words = contents.split()
    len_words = len(words)
    print("The file " + fileName + " has about " + str(len_words) + " words.")
