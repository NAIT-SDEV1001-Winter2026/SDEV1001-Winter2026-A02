def calculate_average(*args):
    return sum(args) / len(args)

def calculate_handicap(*args):
    if len(args) < 5:
        return "Need at least 5 scores to calculate a handicap"
    else:
        top_five = sorted(args)[:5]
        return calculate_average(*top_five) - 72
