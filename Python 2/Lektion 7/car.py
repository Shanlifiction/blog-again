class Car:
    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_info(self):
        return f"Car brand: {self.brand} \nCar model: {self.model} \nCar year: {self.year}"
    
class Child(Car):
    def __init__ (self, brand, model, year):
        super().__init__(brand, model, year)
        self.doors = input("Enter how many doors: ")

    def more_info(self):
        print(f"{self.model} has {self.doors}")

car1 = Child("Porche", "Carrera", 2023)
car1.more_info()