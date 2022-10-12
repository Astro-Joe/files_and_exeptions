import json   

def fav_number():
    # number = fav_number()
    filename = 'fav_number.json'
    try:
        with open(filename) as file:
            current_num = json.load(file)
            print("I know your favorite number! It's " + str(current_num))
    except FileNotFoundError:
        prompt = "Enter your favorite number: "
        filename = 'fav_number.json'
        fav_number = input(prompt)
        with open(filename, 'w') as file:
            json.dump(fav_number, file) 

fav_number()