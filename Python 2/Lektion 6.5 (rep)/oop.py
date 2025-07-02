
#OOP


class Student:
    def __init__ (self, name, age, subject, grade):
        self.__name = name
        self.__age = age
        self.subject = subject
        self.__grade = grade

#dic (mitt i?)
    students = {
        "class": {
            "student_name": "",
            "student_age": ""
        }
    }

    students["class"]["student_name"] = input("Name: ")
    students["class"]["student_age"] = input("Age: ")

    print("Student info: ", students["class"]["student_name"], students["class"]["student_age"])
    print()

#testa lägga till eroor meddelande


    def set_grade(self, grade):
        self.__grade = grade
        print("Grade changed to:", self.__grade)

    def info(self):
        return f"Student name: {self.__name} \nStudent age: {self.__age} \nStudent subject: {self.subject} \nStudent grade: {self.__grade}"

##### 

student1 = Student("Shanli", 33, "Programming", "A")
print(student1.info())
student1.set_grade("A++")





print()

class Library:
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def describe_book(self):
        return f"The author of the book: {self.author} \nThe book title: {self.title} \nRelese year: {self.year}"
    

book1 = Library("AUTHOR", "TITLE", 2000)
print(book1.describe_book())

