class Travels:
    def __init__(self, country, city, year, review):
        self.country = country
        self.city = city
        self.year = year
        self.review = review

    def describe(self):
        return f"{self.country} in {self.city}, {self.year} and {self.review}"
    
travel1 = Travels("Iran", "Urmia", 1991, "I do not remember it.")
travel2 = Travels("Germany", "Hamburg", 1994, "it was memorable. Remember the frog scenario and cute cats!")
travel3 = Travels("France", "Paris", 1996, "I was playing with the twins.")
travel4 = Travels("Finland", "Helsinki", 1997, "it was a cruise ship.")
travel5 = Travels("Denmark", "Legoland", 2002, "it was tgt with father, little brother and friend Lina.")
travel6 = Travels("Denmark", "Copenhagen", 2008, "it was a fun first trip without parents.")
travel7 = Travels("Germany", "Berlin", 2009, "I do not remember it.")
travel8 = Travels("Greece", "Rhodos", 2011, "I do not remember it.")
travel9 = Travels("Turkey", "Alanya", 2012, "I do not remember it.")
travel10 = Travels("Iran", "Urmia", 1991, "I do not remember it.")
travel11 = Travels("Iran", "Urmia", 1991, "I do not remember it.")
travel12 = Travels("Iran", "Urmia", 1991, "I do not remember it.")
travel13 = Travels("Iran", "Urmia", 1991, "I do not remember it.")
travel14 = Travels("Iran", "Urmia", 1991, "I do not remember it.")
travel15 = Travels("Iran", "Urmia", 1991, "I do not remember it.")
travel16 = Travels("Iran", "Urmia", 1991, "I do not remember it.")
travel17 = Travels("Iran", "Urmia", 1991, "I do not remember it.")
travel18 = Travels("Iran", "Urmia", 1991, "I do not remember it.")
travel19 = Travels("Iran", "Urmia", 1991, "I do not remember it.")
travel20 = Travels("Iran", "Urmia", 1991, "I do not remember it.")
travel21 = Travels("Iran", "Urmia", 1991, "I do not remember it.")
print(travel1.country, travel1.city, travel1.year)
print(travel1.describe())