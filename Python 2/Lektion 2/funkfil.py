#skriv ett program som hälsar på namn i fil
#my (first) try
"""
def greet_friends():
    with open("/Users/shanli/desktop/Python 2/Lektion 2/friends.txt", "r") as file:
        file.read()
        for name in file:
            return name
        print("Hello", name, "Have a great wknd!")
"""

#my (second) try
#def greet_friends():
with open("/Users/shanli/desktop/Python 2/Lektion 2/friends.txt", "r") as file:
        #file.read()
        for name in file:
            name = name.strip() #för att inte hälsningen ska hamna på rader under
            #return name
            print("Hello", name + ".", "Have a great wknd!")

#example of one way to do it
"""
with open("/Users/shanli/desktop/Python 2/Lektion 2/friends.txt", "r") as file:
    for line in file:
        line = line.strip()
        print("Hello", line, "Have a great wknd!")
"""

import os
members = ["Samer", "Olivia", "Ove", "Sara"]
if not os.path.exists("/Users/shanli/desktop/Python 2/Lektion 2/my_friends"):
      os.makedirs("/Users/shanli/desktop/Python 2/Lektion 2/my_friends")
with open("/Users/shanli/desktop/Python 2/Lektion 2/my_friends/myfrinds.txt", "w") as file:
    for name in members:
          file.write("Hello " + name + " Welcome!\n")