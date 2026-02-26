from score_calculator import calculate_average, calculate_handicap

if __name__ == "__main__":
    print("Golf Score Calculator")
    scores = []
    playing = True
    while playing:
        score_or_play_again = input("Enter another score (q to quit and calculate)?: ")
        if score_or_play_again == "q":
            break
        else:
            scores.append(int(score_or_play_again))

    print(F"Your average golf score is {calculate_average(*scores)}")
    print("Your handicap is:", calculate_handicap(*scores))
