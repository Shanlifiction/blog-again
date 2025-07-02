#Hemöv. nr.8
#try
with open("/Users/shanli/Desktop/Python 2/Lektion 3/kompisar.txt", "r") as file:
    for name in file:
        name = name.split
        print("Welcome", name)

#ett sätt att skriva programmet
with open ("/Users/shanli/Desktop/Python 2/Lektion 3/kompisar.txt", "r") as file:
    line = file.read()
    names = line.strip().split(",") #dela upp raden baserat på kommatecken
    for name in names:
        print("Hej, " + name.strip() + "! Trevlig helg")