class Student:
    def __init__(self, name, age, grade): #3 parametrar (name age grade)
        self.__name = name
        self.__age = age
        self.__grade = grade

    def get_name(self):
        return self.__name #visa name
    
    def get_grade(self):
        return self.__grade #visa grade
    
#metod för att kollega ska kunna ändra attribut värde
    def set_age(self, age): 
        self.__age = age
        print("Age changed to:\n", self.__age)

    def show_info(self):
        #return self.__name, self.__age, self.__grade #går bra, men print (i facit)
        print(f"\tName: {self.__name} \n\tAge: {self.__age} years old \n\tGrade: {self.__grade}\n")

student1 = Student("Hampus", 20, "A")
print(student1.show_info())
student1.set_age(21)
#print(student1.show_info()) #när print finns i funktionen
student1.show_info() #kalla funktionen som den är ifall print redan finns inom funktionen 