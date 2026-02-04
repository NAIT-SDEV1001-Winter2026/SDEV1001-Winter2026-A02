days_of_week = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday",
                "Saturday"]
days_of_weekend = ("Saturday", "Sunday")

for index, day in enumerate(days_of_week):
    # stop the loop if it's wednesday
    if day == "Wednesday":
        break
    # check if the day has a u
    if "u" in day:
        continue

    print(F"{day} is day number {index + 1} of the week")
    if day in days_of_weekend:
        print(F"{day} is a weekend day")
    else:
        print(F"{day} is a weekday")
