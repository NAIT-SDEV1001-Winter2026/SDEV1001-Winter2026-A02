# Exercises Arrays and Loops

## Exercise 1
1. Create a file named `hobbies.py` in this folder.
2. In that file create a list of the hobbies below in the exact order that they are listed.
Hobbies on the list:
- playing squash
- programming
- reading
- petting cats
- playing golf
- visiting friends
- playing video games
- playing board games
- watching movies
Print out the following in the program.
- length of the list
- the 5th item in the list (remember that the index starts at 0)
- the first four items in the list in a sub list.
- the last three items in the list.
3. Run the program and make sure it works. Sample output should look like the following:
```
$ python hobbies.py
Length of the list
9
Fifth item in the list
playing golf
First four items in the list
['playing squash', 'programming', 'reading', 'petting cats']
last three items in the list
['playing video games', 'playing board games', 'watching movies']
```
4. (optional) You can run `python tests_do_not_touch\test_hobbies.py` to see if your program is working correctly.

## Exercise 2
1. Create a file named `tech_shows.py` in this folder.
2. In that file create a list with the following tv shows and movies in the exact order that they are listed (are they ranked in awesomeness? perhaps)
Shows on the list:
- Silicon Valley
- Halt and Catch Fire
- Blackberry
- The Billion Dollar Code
- Mr. Robot
- The IT Crowd
- WeCrashed
- The Social Network
- Severance
- Pirates of Silicon Valley
3. I want you to get the following information from the list.
- The first item on the list.
- The last item on the list.
- Change "WeCrashed" to "The Dropout"
- Change "The Social Network" to "Black Mirror"
- A part of the list from the 5th item up to (and including) the 9th item and print that out.
4. The output should look like the following:
```
$ python tech_shows.py
The best show is Silicon Valley
The most classic show is Pirates of Silicon Valley
The fourth to ninth shows on the list are:
['The Billion Dollar Code', 'Mr. Robot', 'The IT Crowd', 'The Dropout', 'Black Mirror', 'Severance']
```
5. (optional) You can run `python tests_do_not_touch\test_tech_shows.py` to see if your program is working correctly.


## Exercise 3

1. Create a file named `interesting_cities.py` in this folder.
2. In that file create a list with the following cities in the exact order that they are listed. The cities are:
- Edmonton
- Paris
- Munich
- Berlin
- Amsterdam
- Prague
3. Remove "Edmonton" from the list. Add a city to the list that is input from the user. Sort the list and print out the list. The output should look like the following:
```
Enter a city that interests you: London
Our list of interesting cities in alphabetical order is:
['Amsterdam', 'Berlin', 'London', 'Munich', 'Paris', 'Prague']
```
4. (optional) You can run `python tests_do_not_touch\test_interesting_cities.py` to see if your program is working correctly.

## Exercise 4
1. Create a file named `price_is_right.py` in this folder.
2. create a list with three random prices from 1 to 10 in it. Get input from the user to guess the price. If the user guesses the price correctly, print out "You win!", otherwise print out "You lose!". The output should look like the following:
```
$ python price_is_right.py
Welcome to the Price is Right! Guess the price of this coffee
Guess the price of the item: 10
You lose!
The price were:
[4, 4, 5]
```
another example:
```
$ python price_is_right.py
Welcome to the Price is Right! Guess the price of this coffee
Guess the price of the item: 3
You win!
The price were:
[9, 5, 3]
```
3. (optional) You can run `python tests_do_not_touch\test_price_is_right.py` to see if your program is working correctly.

## Exercise 5 
1. Modify the file `tech_shows.py` from exercise 2 for this exercise. 
2. Loop through the list and for each list print out the top 5 shows in the list. The output from both exercises should now look like this:
```
$ python tech_shows.py
The best show is Silicon Valley
The most classic show is Pirates of Silicon Valley
The fourth to ninth shows on the list are:
['The Billion Dollar Code', 'Mr. Robot', 'The IT Crowd', 'The Dropout', 'Black Mirror', 'Severance']
The top five shows are:
Ranked 1 is: Silicon Valley
Ranked 2 is: Halt and Catch Fire
Ranked 3 is: Blackberry
Ranked 4 is: The Billion Dollar Code
Ranked 5 is: Mr. Robot
```
3. (optional) You can run `python tests_do_not_touch\test_tech_shows_top_5.py` to see if your program is working correctly.


## Exercise 6. 
1. Modify the file `interesting_cities.py` from exercise 3 for this exercise.
2. Loop through the cities and only print out cities that are not in Germany (Munich, Berlin) because we can't visit them (for reasons unknown). The output should look like the following:
```
$ python interesting_cities.py
Enter a city that interests you: Edmonton
Our list of interesting cities in alphabetical order is:
['Amsterdam', 'Berlin', 'Edmonton', 'Munich', 'Paris', 'Prague']
Amsterdam is an interesting city that we can visit
Edmonton is an interesting city that we can visit
Paris is an interesting city that we can visit
Prague is an interesting city that we can visit
```
4. (optional) You can run `python tests_do_not_touch\test_interesting_cities_visitable.py` to see if your program is working correctly.
