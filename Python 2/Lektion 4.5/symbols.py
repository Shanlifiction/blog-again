


symbols = {
    "@": 0,
    "#": 0,
    "!": 0
}

with open ("/Users/shanli/Desktop/Python 2/Lektion 4.5/symbols.txt", "r") as file:
    #try:
        content = file.read()
        for char in content:
            try:
                symbols[char] = symbols[char] +1
            except:
                 print("There are no !, # or @")

print(symbols)
