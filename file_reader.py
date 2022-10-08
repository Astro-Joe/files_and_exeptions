with open('text_files\pi_digits.txt') as file_object:
    contents = file_object.readlines()
    #for line in file_object:
for lines in contents:
    print(lines.rstrip())