# You are developing the functionality that will calculate the number of steps it takes to travel a certain distance in steps

# This in the flow:
# 1. User enters the number of distance to travel in meters
# 2. User is asked if they want to walk, run, or sprint the distance
# 3. If the user walks, they travel 1 step at a time. If they run they travel 2 steps at a time, if they sprint they travel 3 steps at a time.
# 4. Display the number of steps the user takes to travel the distance and the time it takes.

# Notes:
# - It takes 3 steps to travel 1 meter.
# - It takes 15 minutes to travel one kilometer at walking pace

distance = int(input("How many meters are you travelling? "))

while True:
    travel_method = input("Do you want to walk, run, or sprint? ")
    if travel_method == "walk":
        distance_per_step = 1
        break
    elif travel_method == "run":
        distance_per_step = 2
        break
    elif travel_method == "sprint":
        distance_per_step = 3
        break
    else:
        print("That is not a valid option!")

print("You choose to walk.")

minutes_per_meter = 15 / 1000
time_to_travel = (distance * minutes_per_meter) / distance_per_step
steps_travelled = distance / distance_per_step

print(f"It takes you {steps_travelled} steps and {time_to_travel} minutes to travel {distance} meters.")



