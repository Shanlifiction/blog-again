class Person:
    def __init__ (self, years, name):
        self.years = years
        self.name = name

class Teacher(Person): #exakt samma fast parantes till "class Child(Parent):"
    def __init__(self, years, name, subject):
        super().__init__ (years, name) #no "def", no "self"
        self.subject = subject

    def introduction(self):
        print(f"My name is {self.name}, I am {self.years} and I teach in {self.subject}.")
