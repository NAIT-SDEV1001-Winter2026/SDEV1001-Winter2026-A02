from price_is_right_games import guess_items_price

print("Welcome to the Price is Right!")

playing = True
while playing:

    guess = int(input("Guess the price of one of the items (done): "))
    is_correct = guess_items_price(guess)
    if is_correct:
        print("You win!")
    else:
        print("Sorry you lose!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "n":
        playing = False