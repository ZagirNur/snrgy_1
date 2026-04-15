class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def say(self):
        print(self.name, "says", self.sound)

    def info(self):
        print("This is", self.name)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")
        self.breed = breed

    def say(self):
        print(self.name, "(", self.breed, ") barks:", self.sound)

    def fetch(self):
        print(self.name, "fetches the ball")


cat = Animal("Cat", "Meow")
cat.say()
cat.info()

dog = Dog("Rex", "Labrador")
dog.say()
dog.info()
dog.fetch()
