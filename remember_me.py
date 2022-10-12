import json

def get_store_username():
    """Get stored username if possible"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username.title()


def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username.title()

def greet_user():
    """Greet the user by name"""
    username = get_store_username()
    if username:
        print("Is " + username + " your username.")
        response = input("Enter yes/no: ")
        if response.lower() == "yes":
            print("Welcome back, " + username)
        elif response.lower() == "no":
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")


greet_user()