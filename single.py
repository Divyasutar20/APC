class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Animal name: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def getName(self):
        return self.name

dog = Dog("Goldy", "Golden Retriever")
dog.display()
print(f"Dog's name is: {dog.getName()}")