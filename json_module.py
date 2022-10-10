import json
#number = [3,4,5,6,7,8]
filename = 'numbers.json'
with open(filename) as file:
    # json.dump(number, file)
    number = json.load(file)
print(number)
#print(numbers)