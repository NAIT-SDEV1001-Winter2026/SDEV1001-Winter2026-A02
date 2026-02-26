import random

def get_coin_filp():
    random_number = random.randint(0, 1)
    if random_number == 0:
        print("The coin flip was: heads")
        return "h"
    else:
        print("The coin flip was: tails")
        return "t"

def get_user_guess():
    user_guess = input("Guess the coin flip! Enter heads or tails (h/t): ")
    return user_guess


# our code is going to run the function below this line.
if __name__ == "__main__":
    user_guess = get_user_guess()

    random_flip = get_coin_filp()

    if (random_flip == user_guess):
        print("you guessed correct!")
    else:
        print("you guessed wrong!")

