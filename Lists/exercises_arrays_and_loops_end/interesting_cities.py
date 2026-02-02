new_city = input("Enter a city that interests you: ")

interesting_cities = [
    'Edmonton',
    'Paris',
    'Munich',
    'Berlin',
    'Amsterdam',
    'Prague',
]

interesting_cities.remove('Edmonton')
interesting_cities.append(new_city)
interesting_cities.sort()

print("Our list of interesting cities in alphabetical order is:")
print(interesting_cities)

invalid_cities = ('Munich', 'Berlin')

for city in interesting_cities:
    if city in invalid_cities:
        continue
    print(F"{city} is an interesting city that we can visit")

