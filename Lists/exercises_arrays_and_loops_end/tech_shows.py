tech_shows = [
    "Silicon Valley",
    "Halt and Catch Fire",
    "Blackberry",
    "The Billion Dollar Code",
    "Mr. Robot",
    "The IT Crowd",
    "WeCrashed",
    "The Social Network",
    "Severance",
    "Pirates of Silicon Valley",
]

print(F"The best show is {tech_shows[0]}")
print(F"The most classic show is {tech_shows[-1]}")

tech_shows[6] = "The Dropout"
tech_shows[7] = "Black Mirror"

print("The fourth to ninth shows on the list are:")
print(tech_shows[3:9])

print("The top five shows are:")
for index, show in enumerate(tech_shows):
    print(F"Ranked {index + 1} is: {show}")
    if index == 4:
        break
