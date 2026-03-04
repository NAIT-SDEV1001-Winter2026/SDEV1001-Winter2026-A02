def create_pokemon():
    print("Adding pokemon...")
    name = input("Enter a name: ")
    element = input("Enter the type: ")
    level = get_int("Enter the level: ")
    is_legendary = get_bool("Is this pokemon Legendary? (true/false) ")

    details = {
        "element": element,
        "level": level,
        "is_legendary": is_legendary
    }
    return name, details

def level_up(pokemon):
    name = input("Enter the pokemon name: ")
    try:
        pokemon[name]["level"] += 1
    except (KeyError, NameError):
        print("Pokemon not found.")

def get_bool(message="Enter an boolean: "):
    while True:
        value = input(message).lower()
        if value == "true":
            return True
        elif value == "false":
            return False
        else:
            print("Not a valid boolean")

def get_int(message="Enter an integer: "):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Not a valid int")
        