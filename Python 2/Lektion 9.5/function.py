def greet(): #första rader skrivs def functionName, parantes och kolon
    name = input("Enter your name: ") #andra raden kan se olika ut, men oftast skapas en variabel som innehåll läggs i
    message = (f"Hello {name}! Have a great day!\n\n") #tredje raden kan ha ytterligre kompletterande message i denna funktion
    return message #sist men inte mist behöver funktionen ge tillbaka "resultat"

print(greet()) #kalla på funktionen
