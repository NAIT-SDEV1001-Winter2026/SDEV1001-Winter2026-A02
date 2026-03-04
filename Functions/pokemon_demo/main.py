from poke_package.poke_helper import create_pokemon, level_up

pokemon = {}

while True:
    choice = input("""
    1. Add Pokemon
    2. Poke-Details
    3. Quit
    4. Level Up Pokemon
    Choice: """)

    match choice:
        case "1":
            new_pokemon_name, new_pokemon_details = create_pokemon()
            pokemon[new_pokemon_name] = new_pokemon_details
        case "2":
            for key in pokemon:
                print(key)
                details = pokemon[key]
                for k, v in details.items():
                    print(f"   - {k}: {v}")

        case "3":
            break
        case "4":
            level_up(pokemon)
        case _:
            print("Invalid option...")