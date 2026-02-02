import random

random_prices = [
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10),
]

print("Welcome to the Price is Right! Guess the price of this coffee")
guess = int(input("Guess the price of the item: "))

if guess in random_prices:
    print("You win!")
else:
    print("You lose!")

print("The price were: ")
print(random_prices)