

class Car:
    def __init__(self, brand, model, year, speed): #speed kan skrivas speed=0.0
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0.0 #ej skriva "speed"

    def describe(self):
        return f"Car: {self.brand} {self.model} from: {self.year}" #no need "speed: {self.speed}"
    
    def drive(self, input_speed): #input_speed är parameter
        self.speed = input_speed #anger bilens hastighet till "input_speed"
        #return f"Car: {self.brand} speed: {self.speed}"
    
    def stop(self):
        self.speed = 0.0 #stillastående bil
        #return

### OUTSIDE OF CLASS ###
#skapa/generera objekt
car1 = Car("Toyota", "Corolla", 2022, 0.0) 
car2 = Car("Honda", "Civic", 2021, 0.1)

print(car1.describe())
print(car2.describe())
#print(car1.drive(50), car1.speed) #50 är "input_speed"
#print(car2.drive(51), car2.speed)
car1.drive(50)
#print (f"{car1.speed} drives {car1.drive} Km/h.")
print(f"{car1.describe()} drives {car1.speed} Km/h")
car2.drive(51)
#print(f"{car2.speed} drives {car2.drive} Km/h.")
print(f"{car2.describe()} drives {car2.speed} Km/h")

car1.stop()
print(f"{car1.describe()} stops {car1.speed} Km/h")



