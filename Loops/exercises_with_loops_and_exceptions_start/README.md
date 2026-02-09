# Exercises Loops and Exceptions

## Exercise 1
1. create a file named `sum_of_squares.py` in this folder.
2. Find the sum of squares of the integers from 1 to `my_square`, where `my_square` is a variable that is input by the user. E.g. user enters 4 then return 1x1 + 2x2 + 3x3 + 4x4 = 30

3. The output should look like the following:
```
$ python sum_of_squares.py
Enter a number to sum the squares: 4
The sum of squares is 30
```
4. (optional) You can run `python tests_do_not_touch\test_sum_of_squares.py` to see if your program is working correctly.

## Exercise 2.
1. create a file named `vowel_counter.py` in this folder.
2. Using your knowledge that strings are also lists in python count the number of vowels that are in a string from the user.
3. The output should look like the following:
```
$ python vowel_counter.py
Enter a word for us to count vowels: onomatopoeia
o
n
o
m
a
t
o
p
o
e
i
a
There are 8 vowels in onomatopoeia
```
4. (optional) You can run `python tests_do_not_touch\test_vowel_counter.py` to see if your program is working correctly.

## Exercise 3
1. Create a file named `average_age_of_students.py` in this folder.
2. Create a program that's going to continously ask the user for the age of a student until the user enters `stop`. Once the user enters `stop` then print out the average age of all the students.
3. The output should look something like this.
```
$ python average_age_of_students.py
Average age of students calculator
Enter the age of a student or 'stop' to finish: 10
Enter the age of a student or 'stop' to finish: 12
Enter the age of a student or 'stop' to finish: 14
Enter the age of a student or 'stop' to finish: 20
Enter the age of a student or 'stop' to finish: stop
The average age of the students is 14.0
```


## Exercise 4
1. Create a file named `isp_prices.py` in this folder.
2. Write a program for an Internet Service Provider so they can calculate the monthly bill for their customers. The following three packages look like the table (shown below). The program should ask the user for the package and the number of hours they have used. Then it should print out the amount 

|PACKAGE| COST CALCULATION|
|-------|-----------------|
|A | $9.95 per month for 10 hours additional hours are billed at $2.00 per hour|
|B | $13.95 per month for 20 hours; additional hours are billed at $1.00 per hour |
|C | $19.95 per month of unlimited hours|

3. Output should look like the following
- package A output
```
$ python isp_prices.py
Enter the package: A
Enter the number of hours used: 15
The total price is $19.95
```
- package B output
```
$ python isp_prices.py
Enter the package: B
Enter the number of hours used: 25
The total price is $18.95
```
- package C output
```
$ python isp_prices.py
Enter the package: C
Enter the number of hours used: 9001
The total price is $19.95
```
4. (optional) You can run `python tests_do_not_touch\test_isp_prices.py` to see if your program is working correctly.


## Exercise 5
1. Modify the file `average_age_of_students.py` from exercise 3 for this exercise.
2. If the user enters anything else than a number then print out "Please enter a number or 'stop' to finish". As well handle the case where the user doesn't add any ages, and print out the following "You didn't enter any ages".
3. The output should look something like this.
```
$ python average_age_of_students.py
Average age of students calculator
Enter the age of a student or 'stop' to finish: five
Please enter a valid age or 'stop' to finish.
Enter the age of a student or 'stop' to finish: stop
You didn't enter any ages to average
```
4. (optional) You can run `python tests_do_not_touch\test_average_age_of_students_exceptions.py` to see if your program is working correctly.

## Exercise 6
1. Modify the file `isp_prices.py` from exercise 4 for this exercise.
2. If the user enters anything else than a number then print out "Please enter a number for the hours used". As well handle the case where the user doesn't add any hours, and print out the following "You didn't enter any hours". Note for the program not to crash you'll need to set the number of hours to 0 if the user doesn't enter the hours correctly
3. The output should look something like this.
```
$ python isp_prices.py
Enter the package: A
Enter the number of hours used: twenty
Please enter a valid number of hours
The total price is $9.95
```
4. (optional) You can run `python tests_do_not_touch\test_isp_prices_exceptions.py` to see if your program is working correctly.
