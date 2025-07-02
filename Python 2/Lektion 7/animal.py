class Animal:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        #eat = input("Enter what the animal has eaten: ")
        #print(f"Animal eat: {eat}")
        print(f"{self.name} is eating.")

    def sleep(self):
        #pass
        print(f"{self.name} is sleeping.")

    def make_noise(self):
        print(f"{self.name} makes noise.")

animal1 = Animal("Apa", 3)
animal1.eat()

class Dog(Animal):
    def __init__ (self, name, age, sort):
        super().__init__(name, age)
        self.sort = sort

    def bark(self):
        #pass
        print(f"{self.name} is barking.")

    def made_noise(self): #ersätter metod från parent-klassen
        self.bark()

    def show_sort(self):
        print(f"{self.name} is a {self.sort}")