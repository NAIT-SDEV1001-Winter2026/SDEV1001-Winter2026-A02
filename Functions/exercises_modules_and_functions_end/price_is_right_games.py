import random

def guess_items_price(guess):
    """
    Guess the price of the item.
    returns True if the guess is correct, False otherwise
    """
    random_prices = [
        random.randint(1, 10),
        random.randint(1, 10),
        random.randint(1, 10),
    ]
    print(F"The prices were: {random_prices}")

    if guess in random_prices:
        return True
    else:
        return False

def guess_car_price(guess):
    """
    Guess the price of the car.
    returns True if the guess is correct, False otherwise
    """
    car_price = random.randint(10000, 50000)
    
    print(F"The price of the car was: {car_price}")

    if guess == car_price:
        return "You win! That's exactly the price! You're a cheater!"
    elif guess > car_price -1000 and guess < car_price + 1000:
        return "You win!"
    elif guess > car_price -5000 and guess < car_price + 5000:
        return "You're close!"
    else:
        return "Sorry you lose!"