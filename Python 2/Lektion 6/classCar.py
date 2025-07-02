#Getter/Setter

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

#getter method (utanför klassen) läs värdet genom denna metod, men ej ändra
    def get_brand(self):
        return self.__brand #return tillverkar av car

#setter method (utanför klassen) ändra värdet blir möjligt
    def set_model(self, model):
        self.__model = model
        print("Model change:", self.__model)

########################## OUTSIDE CLASS
#skapa objekt/instans
car1 = Car("Porsche", "Carrera")
print(car1.get_brand())
car1.set_model("C64")
#print(car.__brand)     #ej möjligt att nå detta privata attribut