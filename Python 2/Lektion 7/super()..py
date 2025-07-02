class Person: #PARENT
    def __init__ (self, first, last):
        self.first = first #addera attribut
        self.last = last
    
    def full_name(self):
        print()
    
person1 = Person("Anna", "Andersson")
print(person1.full_name())

class Student(Person): #CHILD ärver egenskaper & metoder från PARENT
    def __init__ (self, first, last, age):
        super().__init__(first, last) #super(). lägger till ny parameter
        self.age = age #addera nytt attribut

    def show_info(self):
        print(f"Name: {self.first}{self.last} \nYear: {self.age}")

student1 = Student("Mike", "Olsen", 35)
student1.show_info()

