class Person:
    def __init__(self, firstn, lastn):
        self.firstn = firstn
        self.lastn = lastn

    def show_name(self):
        print(self.firstn, self.lastn) 

#UTANFÖR SKAPAS OBJEKT
#PRINT PARENT
    
person1 = Person("Monica", "Göransson")
print(person1.show_name())

#ARV
#CHILD CLASS
    
class Student(Person):
    pass

student1 = Student("Mike", "Olsen")
#print()