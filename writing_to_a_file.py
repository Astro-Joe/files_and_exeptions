fileName = 'learning_python.txt'

# For opening a file in read mode.
# When a file is opened in write mode its writes over all existing contents
with open(fileName, 'w') as file_object:
    file_object.write("I love python.\n")
    # Write mode allows writing of multiple lines.
    file_object.write("It's very cool.\n")

# For opening a file in read mode.
# with open(fileName, 'r') as file_object:
#     file_object.write("\nI love python")

# For opening a file in append mode.
# with open(fileName, 'a') as file_object:
#     file_object.write("\nI love python")

# For reading he content of a file   
with open(fileName) as someWhat:
    contents = someWhat.read()
    print(contents.rstrip())