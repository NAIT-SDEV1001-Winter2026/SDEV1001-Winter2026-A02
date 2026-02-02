# our grocery list.
groceries = ['lettuce', 'tomatoes', 'bread', 'milk', 'chicken', 'apples']
print("Our grocery list is: ")
print(groceries)

# Modifying items in the list.
groceries[0] = 'romaine lettuce' # changing the first item
groceries[2] = 'baguette' # changing the third item
print("Our modified grocery list is: ")
print(groceries)

# Let's check the first item in our list.
print("the first item in our grocery list is: ")
print(groceries[0])
# Let's check out the third item in our list.
print("the first item in our grocery list is: ")
print(groceries[2])


# Slicing lists.
print("The first three items in our list are: ")
print(groceries[0:3]) # this will print the first three items in the list.

print("The last two items in our list are: ")
print(groceries[-2:]) # this will print the last two items in the list.

# Getting the length of a list.
print("The length of our grocery list is: ")
print(len(groceries)) # this will print the length of the list.
