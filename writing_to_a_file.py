fileName = 'learning_python.txt'
with open(fileName, 'r') as file_object:
    file_object.write("\nI love python")

# with open(fileName, 'r') as file_object:
#     file_object.write("\nI love python")

# with open(fileName, 'a') as file_object:
#     file_object.write("\nI love python")
    
with open(fileName) as someWhat:
    contents = someWhat.read()
    print(contents)