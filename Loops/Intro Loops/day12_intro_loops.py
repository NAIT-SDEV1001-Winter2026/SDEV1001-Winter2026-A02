#List Comprehension
# List comprehension is a very powerful tool in python that allows us to significantly reduce the lines of code required to create sublists.

# The format for using it is:
# new_list = [<var> for <var> in <old_list> <logic>]

# For example, list comprehension can turn this code:

weapons = ["shotgun", "knife", "sword", "BB gun", "water gun"]
guns = []

for weapon in weapons:
    if "gun" in weapon:
        guns.append(guns)

print(guns)

# into this code:

guns = [weapon for weapon in weapons if "guns" in weapon]

print(guns)

# List comprehension is useful when we want a subset of items from a list. 

# STRINGS ARE CHARACTER ARRAYS
# The string data type is actually a list of individual characters. and since that is the case, we can loop through the characters in a string just like a list:

for ch in "Hello":
    print(ch)

inventory = ["knife of cutting", "shotgun of true love", "pez dispenser of forgiveness", "kleenex of neverending doom", "fidget spinner of time"]

# to print all of the items in our lists, we can use the for loop with the following structure:
# for <variable> in <list>:
#     do something with the variable

# the <variable> is a new variable that will exist only in the context of the for loop. The for loop looks at each item individually and assigned the value of the current item to <variable>

# To loop through all of the items in our inventory and print them to the console:
print("Our inventory contains:")
for item in inventory:
    print(f"- {item}")

# don't forget to indent.

# a tuple is a special type of list. Unlike our normal lists, they cannot be changed. We create a tuple the same way we create a list, except we use parentheses () instead of square brackets []

available_liquids = ["acid", "water", "soda", "bleach", "liquid nitrogen"]

# This is an unchangeable list of liquids that are safe to drink.
drinkable_liquids = ("water", "vinegar", "coffee", "soda")

for liquid in available_liquids:
    if liquid in drinkable_liquids:
        print(f"You can drink {liquid}.")
    else:
        print(f"You can drink {liquid}, but you probably shouldn't...")

# Tuples also allow us to return multiple items from a function, which is a useful trick.

# Python provides us with a way to get the both the value of an item as well as its index.
# We do this using the built-in enumerate() function.

# The syntax for this is:
# for <variable_for_index>, <variable_for_value> in enumerate(<list>)

# The first variable we declare here will be to hold the index, and the second to hold the value.

# to list the items in our inventory as well as the index:

for idx, item in enumerate(inventory):
    print(f"{idx}. {item}")


# CONTINUE
# The continue statement is used when we want to skip the rest of the code in loop. If the continue statement is reached, then the code will immediately move to the next iteration of the loop.

# For example, the following code will print only odd numbers, and skip any even numbers.

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        continue #skips any remaining code and moves to next iteration
    print(f"Odd number: {n}")


# BREAK
# The break statement will abort the execution of a loop. The term "break out" is used to describe this behavior. When the break statement is reached, the loop immediately stops running and moves on the next line of execution outside of the loop.

# for example, the following code will execute until the animal is a parrot

animals = ["dog", "cat", "goose", "hamster"]
for animal in animals:
    if animal == "goose":
        print("There is a goose. They can be jerks so we better leave immediately.")
        break
    print(f"A cute little {animal}")

# WHILE LOOPS

# A while loop is a loop that will execute so long as a particular condition is true. While loops are everywhere in software development, and definitely with games. Every game is running inside of a while loop. We play the game until the player desides to quit.

playing = True
while playing:
    print("Pew pew!")
    keep_playing = input("Do you want to keep playing? (y/n)")
    if keep_playing == "n":
        playing = False

# Do-while Loops
# Python does not have a built-in do-while data structure, unlike some other programming languages like C# and java.
# To implement the Do-While data structure in Python, we need to use a while loop with the exit condition of True. This will guarantee that the loop executes. Then to stop the loop, we use break statements as our exit conditions.

# Here is the same example of a game loop using the do-while structure
while True:
    print("Pew pew!")
    keep_playing = input("Do you want to keep playing? (y/n)")
    if keep_playing == "n":
        break

