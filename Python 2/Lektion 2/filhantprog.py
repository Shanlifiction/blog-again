#skapa fil och skriv 3 textrader
with open("/Users/shanli/desktop/Python 2/Lektion 2/filhantex.txt", "w") as file: #w for write
    file.write("Hello World!\n This is a text.\n Good bye!")
#print("D for Done.")

#läs in innehållet
with open("/Users/shanli/desktop/Python 2/Lektion 2/filhantex.txt", "r") as file: #r for read
    content = file.open()

#lägg till text
with open("/Users/shanli/desktop/Python 2/Lektion 2/filhantex.txt", "a") as file: #a for append
    file.open("/Users/shanli/desktop/Python 2/Lektion 2/filhantex.txt")
