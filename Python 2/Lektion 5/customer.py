


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"Hello {self.name}, {self.age}!"
    
### OUTSIDE OF CLASS ###
cus1 = Customer("Shanli", 33) #first object
cus2 = Customer("Alice", 30) #second object etc
print(cus1.name, "\n" + 
      cus2.name)