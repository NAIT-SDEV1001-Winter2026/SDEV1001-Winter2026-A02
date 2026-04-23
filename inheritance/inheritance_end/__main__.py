from animals import Animal, Dog, Cat, Bird

def main():
    dog = Dog("Ranger", "Brown", 4, "Labrador")
    cat = Cat("Soul Destroyer", "Black", 4, "Tabby", 25)
    bird = Bird("Furbird", "Green", 2, 40.0)

    animals = [dog, cat, bird]

    for animal in animals:
        print("-----------------")
        print(animal)
        
        animal.make_a_noise()
        animal.move()
        animal.eat()

        if isinstance(animal, Dog):
            animal.chase_car()
        
        if isinstance(animal, Cat):
            animal.knock_stuff()

        print("-----------------")

if __name__ == "__main__":
    main()