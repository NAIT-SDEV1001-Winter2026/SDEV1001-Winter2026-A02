my_square = input("Enter a number to sum the squares: ")

total = 0

for number in range(int(my_square)):
    total += (number+1) ** 2

print(F"The sum of squares is {total}")
   