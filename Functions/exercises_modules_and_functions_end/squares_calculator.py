def calculate_sum_of_squares(num):
    total = 0
    for number in range(num):
        total += (number+1) ** 2
    return total