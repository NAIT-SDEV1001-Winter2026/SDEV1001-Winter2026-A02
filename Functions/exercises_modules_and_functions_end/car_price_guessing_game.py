from price_is_right_games import guess_car_price

print("Welcome to the car price guessing game!")

playing = True
while playing:
    guess = int(input("Guess the price of the car: "))
    result = guess_car_price(guess)
    print(result)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "n":
        playing = False