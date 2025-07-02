#import os

with open ("/Users/shanli/Desktop/Python 2/Lektion 9.5/friends.txt", "r") as file: #första raden innehåller "with open" ["PATH", tex "r"] as file & kolon"
    #content = file.read()
    for name in file: #andra raden kan vara en loop
        name = name.strip() #skapa och spara variabel
        print(f"Hello {name}!") #printa ut "jobbet"

    