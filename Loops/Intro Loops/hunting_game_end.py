import random

HIT_LIMIT = 9

available_monsters = ("zombie", "wraith", "bandit", "ghoul", "sphinx", "venemous gerbil", "chimera")
weapons = ["crossbow", "nail clippers", "knife", "gun", "rubber chicken", "vitamins", "sword"]

active_monsters, defeated_monsters = [], []
health = 5

while True:
    
    #check here IndexError exceptions
    monster_index = random.randint(0, len(available_monsters) - 1)
    monster = available_monsters[monster_index]
    active_monsters.append(monster)
    print(f"A {monster} spawns!")
    print("The following monsters are running at you:")
    for m in active_monsters:
        print(f"- {m}")
    
    for idx, m in enumerate(active_monsters):
        print(f"You choose to attack the {m}")
        weapons_count = len(weapons)
        if weapons_count == 0:
            print("Oh no you're out of weapons! Escape!")
            break
        valid_choice = False
        while not valid_choice:
            weapon = input("Choose your weapon: ").lower()

            if weapon in weapons:
                print(f"You pull out your trusty {weapon}")
                valid_choice = True
            else:
                print(f"You forgot your {weapon}! Choose something else.")
        
        print(f"You attack with the {weapon}")

        roll = random.randint(1, 12)
        if roll >= HIT_LIMIT:
            print(f"Critical hit! Monster {idx + 1} goes down.")
            defeated_monsters.append(m)
            print(f"You're {weapon} disintegrates...")
            weapons.remove(weapon)
        else:
            print(f"Oh no you miss. The {m} attacks you!")
            health -= 1
    
    if (health < 1):
        print("You're dead.")
        break

    for m in defeated_monsters:
        m_index = active_monsters.index(m)
        del active_monsters[m_index]
    
    keep_hunting = input("Would you like to keep hunting? (y/n) ")
    if not keep_hunting:
        print("Hunting trip over. Back to the grind.")
        break
    
    defeated_monsters.clear()

