with open ("/Users/shanli/Desktop/Python 2/Lektion 4 (rep)/textfil.txt", "r") as file:
    for name in file:
        name = name.strip()
        print("Hello", name + ". Hope all is well!")
