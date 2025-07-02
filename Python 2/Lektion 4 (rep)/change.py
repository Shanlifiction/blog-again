def change_letter(text):
    var = ""
    for letter in text:
        if letter == "Ö":
            var = var + "O"
        elif letter == "ö":
            var = var + "o"
        elif letter == "Ä" or letter == "Å":
            var = var + "A"
        elif letter == "ä" or letter == "å":
            var = var + "a"
        #elif letter == "Å":
            #var = var + "A"
        #elif letter == "å":
            #var = var + "a"
        else:
            var = var + letter
    return var
        
print(change_letter("Örter är ömtåliga"))

