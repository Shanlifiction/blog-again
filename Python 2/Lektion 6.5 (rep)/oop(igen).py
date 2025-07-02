#Dic
student_class_list = {
    "class": {
        "name": "",
        "age": ""
    }
}

student_class_list["class"]["name"] = input("Student name: ")
student_class_list["class"]["age"] = input("Student age: ")

print(student_class_list["class"]["name"])
print(student_class_list["class"]["age"])



#OOP
class Books:
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def describe_book(self):
        return f"Book author: {self.author} \nBook title: {self.title} \nBook relese: {self.year}"
    
book1 = Books("AUTHOR", "TITLE", 2000)
print(book1.describe_book())