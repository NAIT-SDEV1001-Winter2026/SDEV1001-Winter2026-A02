import random

songs = ["Valentine", "Iron Man", "Thriller", "Moves Like Jagger", "Pickles from the Jar"]

songs.append("Soothsayer")

for song in songs:
    print(f"- {song}")

# Forgot about Dre
print("----------------------")

songs.insert(2, "Forgot About Dre")

index = 0
for song in songs:
    print(f"{index}. {song}")
    index += 1

print("----------------------")

songs.sort(reverse=True)

for song in songs:
    print(f"- {song}")

random.shuffle(songs)

print("----------------------")
for song in songs:
    print(f"- {song}")

pop(), remove

song_popped = songs.pop(3)
print(songs)
print(f"Song removed: {song_popped}")

if "Soothsayer" in songs:
    songs.remove("Soothsayer")
print(songs)

length = len(songs)
print(f"{length} songs in list.")

item_index = songs.index("Valentine")
print(f"Valentine is at index: {item_index}")

songs.clear()
print(songs)