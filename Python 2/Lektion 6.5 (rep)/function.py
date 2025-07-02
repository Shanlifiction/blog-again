"""
def change_letter(text):
    var = ""
    for letter in text:
        if letter == "ö":
            var = var + "o"
        elif letter == "Ö":
            var = var + "O"
        else:
            var = var + letter
    return var
    
print(change_letter("Östermalm är österut!"))
"""



def change_letter(text):
    var = ""
    for letter in text:
        if letter == "Ö":
            var = var + "O"
        elif letter == "ö":
            var = var + "o"
        else:
            var = var + letter
    return var

print(change_letter("Östermalm är österut!"))



def change_letter(text):
    var = ""
    for letter in text:
        if letter == "Ö":
            var = var + "O"
        elif letter == "ö":
            var = var + "o"
        else:
            var = var + letter
    return var

print(change_letter("Det ligger öster om Östermalm"))