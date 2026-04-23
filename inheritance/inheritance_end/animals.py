class Animal:
    def __init__(self, name, color, num_legs):
        self.name = name
        self.color = color
        self.num_legs = num_legs

    def eat(self):
        print(f"{self.name} starts eating. Nom nom nom...")

    def make_a_noise(self):
        print(f"{self.name} makes an interesting noise.")

    def move(self):
        print(f"{self.name} runs around!")

    def __str__(self):
        return f"Name: {self.name}\nColor: {self.color}\nNumber of Legs: {self.num_legs}"

    def __repr__(self):
        return f"Animal(name={self.name}, color={self.color}, num_legs={self.num_legs})"

class Dog(Animal):
    def __init__(self, name, color, num_legs, breed):
        super().__init__(name, color, num_legs)
        self.breed = breed

    def __str__(self):
        super_string = super().__str__()
        super_string += f"\nBreed: {self.breed}"
        return super_string

    def make_a_noise(self):
        print(f"{self.name} starts barking loudly! Bark Bark!")

    def chase_car(self):
        print(f"{self.name} chases after a Honda Civic!")

class Cat(Animal):
    def __init__(self, name, color, num_legs, pattern, anger_level):
        super().__init__(name, color, num_legs)
        self.pattern = pattern
        self.anger_level = anger_level

    def __str__(self):
        super_string = super().__str__()
        super_string += f"\nPattern: {self.pattern}"
        return super_string

    def make_a_noise(self):
        if self.anger_level > 20:
            print(f"{self.name} says Hiss!")
        elif 10 < self.anger_level <= 20:
            print(f"{self.name} says meow meow.")
        else:
            print(f"{self.name} says purr purr.")

    def knock_stuff(self):
        print(f"{self.name} knocks a clock off of the shelf.")

class Bird(Animal):
    def __init__(self, name, color, num_legs, wingspan):
        super().__init__(name, color, num_legs)
        self.wingspan = wingspan

    def __str__(self):
        super_string = super().__str__()
        super_string += f"\nWingspan: {self.wingspan} cm"
        return super_string

    def make_a_noise(self):
        print(f"{self.name} says 'I want crackers.'")

    def eat(self):
        print(f"{self.name} pecks at the crackers.")

    def move(self):
        print(f"{self.name} flies around!")