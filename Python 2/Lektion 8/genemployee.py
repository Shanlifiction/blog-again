class General:
    def __init__ (self):
        self.name = input("Enter employees name: ")
        self.salary = input("Enter salary: ")
        self.department = input ("Enter department: ")
        print(f"\nName: {self.name} \nSalary: {self.salary} \nDepartment: {self.department}\n")

    def info(self):
        self.name = input("Enter employees name: ")
        self.salary = input("Enter salary: ")
        self.department = input ("Enter department: ")

class Boss(General):
    def __init__(self):
        super().__init__ ()
        self.level = input("Enter employee level: ")
