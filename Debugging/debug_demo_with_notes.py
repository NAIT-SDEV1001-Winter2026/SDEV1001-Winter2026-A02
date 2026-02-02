# To create a breakpoint, click in the whitespace to the LEFT of the line number. It is a little red dot.
# Breakpoints pause the program at the spot BEFORE the highlighted line is executed

# Debugger Shortcuts and Explanations:
# Continue (F5) - Play arrow - Will execute the rest of the code until the next breakpoint is hit or the program ends
# Step Over (F10) - Arrow jumping over dot - Will execute the currently highlighted line of code and move to the next line in the logical sequence
# Step Into (F11) - Down arrow - Will enter the code of a function if it is called, otherwise it will be the same as Step Over
# Step Out (Shift + F11) - Up arrow - If debugging inside of a function, it will execute the rest of the function and move to the next logical sequence where the function was called.
# Restart (Shift + Ctrl + F5) - Restart the program in debug mode
# Stop (Shift + F5) - Abort the program

# The variable window on the left will keep track of any variables currently in use.,


def my_demo_function(number):
    print("Hello my friend!")
    print("You are inside my_demo_function()")
    print(f"You have entered the number {number} ")
    print("Leaving my_demo_function()")

user_input = int(input("Enter a number: "))

if user_input < 0:
    print("That number is negative.")
elif user_input < 10:
    print("That number is pretty small.")
elif user_input < 100:
    print("That number is a little bit bigger.")
else:
    print("That number is huge!")

print("Let's perform some math on that number")

user_input += 10000
user_input *= 3
user_input /= 5

my_demo_function(user_input)
my_demo_function(user_input * 2)
my_demo_function(user_input * 3)
my_demo_function(user_input * 4)

my_list = [5, 1, 30, 55, 11]

print(my_list)