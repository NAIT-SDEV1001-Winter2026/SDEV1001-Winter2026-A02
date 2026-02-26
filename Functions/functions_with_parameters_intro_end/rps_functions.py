def translate_number_to_choice(number):
    choice = ""
    if number == 0:
        choice = "scissor"
    elif number == 1:
        choice = "rock"
    elif number == 2:
        choice = "paper"
    return choice

# checks if the player choice wins
def is_winner(player_choice, opponent_choice):
    return ((player_choice == "paper" and opponent_choice == "rock") or 
        (player_choice == "rock" and opponent_choice == "scissor") or
        (player_choice == "scissor" and opponent_choice == "paper"))

def get_game_result(user_input, computer_input):
    user_result = translate_number_to_choice(user_input)
    computer_result = translate_number_to_choice(computer_input)

    # tie
    if user_result == computer_result:
        print(F"The computer is {computer_result}. You are {user_result}. It is a draw")
        return "tie"
    # user wins
    elif is_winner(user_result, computer_result):
        print(F"The computer is {computer_result}. You are {user_result}. You win")
        return "user wins"
    # computer wins
    elif is_winner(computer_result, user_result):
        print(F"The computer is {computer_result}. You are {user_result}. You lose")
        return "computer wins"
