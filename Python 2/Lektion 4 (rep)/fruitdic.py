fruits = {
    "Apple": 10,
    "Banana": 15,
    "Mandarin": 20,
    "Pear": 25
}
choose = input("Choose a fruit (Apple, Banana, Mandarin or Pear) to see how many there are. Prick your choice or write all: ").capitalize()
try:
    print(fruits[choose])
except KeyError:
    if choose == "All": 
        print(fruits)
    else:
        print("The fruit does not exist. Try again!")
#else:
    #if input("All").capitalize(): #input har redan skrivit en gång och omvandlats till en variabel (choose). Använd den variabeln!!!
        #print(fruits) 
        # HÄR KAN MAN SKRIVA NÅGOT SOM SKA GÖRAS OM ERROR EJ FINNS/TRY EJ BEHÖVS?


"""
svar = input ("Är patienten ett barn? Y/N ").upper() #genom funktionen .upper() tolkar/omvandlas små bokstäver till stora
if svar == ("Y"):
    print ("Patienten ska ha 500mg per dag.")
else:
    print ("Patienten ska ha 750mg per dag.")
"""


#skulle repa och råkade mixa dictionary med en function. Blev helt åt pipsvängen heheh
"""
def my_fruits(): {
    "apple": 30,
    "banana": 15,
    "melon": 10,
    "orange": 20,
    "pear": 25
}

answer = input("There are fruits in this basket. Name a fruit: ")
try:
    answer == fruit
    print(my_fruits(fruit))
except ValueError:
    if answer == ("All").capitalize:
        print(my_fruits)
else:
    print("")

my_fruits()
"""