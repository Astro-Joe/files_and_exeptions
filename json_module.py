import json


numbers = [2, 3, 5, 7, 11, 13]
with open('numbers.json','w') as file:
    json.dump(numbers, file)