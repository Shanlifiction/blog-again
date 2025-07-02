#del1   metod init: används för att initialisera objekt med startvärden / parametrar
class Book:
    def __init__ (self, title, author, year): #init metod
    #self måste alltid vara första parametern inom alla metoder. 
    #Detta är för att berätta för programmet att metoden tillhör ett objekt i klassen.
        #attribut = parametrar
        self.title = title
        self.author = author
        self.year = year

#del2   metod (denna klass har endast en metod)
    def describe(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
#utanför generaras objekt / instans
book1 = Book("TITLE", "AUTHOR", 2025)   #object
print(book1.title)                      #skriver ut title only
print(book1.describe())                 #kallar på metoden describe för att returnera alla tre attribut