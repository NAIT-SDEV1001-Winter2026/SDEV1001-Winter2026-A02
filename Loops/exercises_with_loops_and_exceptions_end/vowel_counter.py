word = input("Enter a word for us to count vowels: ")

total = 0 
for character in word:
    print(character)
    if character.lower() in 'aeiou':
        total += 1

print(f"There are {total} vowels in {word}")