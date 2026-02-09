print("Average age of students calculator")

total_age = 0
count = 0 
while True:
    age = input("Enter the age of a student or 'stop' to finish: ")

    if age == "stop":
        break
    else:
        try:
            total_age += int(age)
            count += 1
        except ValueError:
            print("Please enter a valid age or 'stop' to finish.")
try:
    print(f"The average age of the students is {total_age/count}")
except ZeroDivisionError:
    print("You didn't enter any ages to average")