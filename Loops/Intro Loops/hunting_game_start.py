import random
import time

HIT_LIMIT = 9

available_monsters = ("zombie", "wraith", "bandit", "ghoul", "sphinx", "venemous gerbil", "chimera")
weapons = ["crossbow", "nail clippers of death", "knife", "gun", "rubber chicken", "vitamins", "sword"]

health = 5
active_monsters, defeated_monsters = [], []

while True:
    monster_index = random.randint(0, len(available_monsters) - 1)
    monster = available_monsters[monster_index]
    active_monsters.append(monster)

    print(f"A {monster} has appeared!")
    print("The following monsters are attacking you: ")

    for attacking_monster in active_monsters: 
        print(attacking_monster)

    for idx, current_monster in enumerate(active_monsters):
        print(f"You attack the {current_monster}!")

        if len(weapons) == 0:
            break
            
        valid_choice = False
        while not valid_choice:
            print(f"Your available weapons: {weapons}")
            weapon_choice = input("Which weapon will you choose? ").lower()

            if weapon_choice in weapons:
                print(f"You pull out your trusty {weapon_choice}")
                valid_choice = True
            else:
                print(f"You forgot your {weapon_choice}")
        
        print(f"You attack the {current_monster} with a {weapon_choice}!")

        dice_roll = random.randint(1, 12)

        if dice_roll >= HIT_LIMIT:
            print(f"You smite the {current_monster} with a {weapon_choice}!")
            defeated_monsters.append(current_monster)
            time.sleep(2)
            print(f"Your {weapon_choice} disintegrates...")
            weapons.remove(weapon_choice)
        else:
            print(f"Oh no you miss! The {current_monster} attacks you!")
            health -= 1

    if len(weapons) == 0:
        print("You have no weapons! Run awaaaaawaay!")
        break
    
    if health <= 0:
        print("Ya dead!")
        break

    for m in defeated_monsters:
        m_index = active_monsters.index(m)
        del active_monsters[m_index]

    keep_hunting = input("Do you want to keep hunting? (y/n) ").lower()

    if keep_hunting == "n":
        print("Back to the grind...")
        break
    
    print("Lock and load!")

    defeated_monsters.clear()

    