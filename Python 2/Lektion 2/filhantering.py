#file = ""

file = open("/Users/shanli/Desktop/Python 2/Lektion 2/python.txt", "a")

file.write("I like python.")

file.close()


file = open("/Users/shanli/Desktop/Python 2/Lektion 2/python.txt", "r")
newfile = (file.read())
print(newfile)
#print(file.read()) går också bra istället för att skapa en ny variabel (i detta fall newfile)

file.close()


#upg3
import os #remove ligger i ett bibliotek därför behöver os importeras
if os.path.exists("/Users/shanli/desktop/Python 2/Lektion 2/python1.txt"):
    os.remove("/Users/shanli/desktop/Python 2/Lektion 2/python1.txt")    #fungerar ej!!! Jo, ett s saknades i "/Users"
    print("File has been removed")
else:
    print("File does not exist.")


#with-satsen
with open("/Users/shanli/Desktop/Python 2/Lektion 2/python.txt", "r") as file:
    content = file.read()
print("The content in this file is:", content)

#arbeta i ram-minnet
with open("/Users/shanli/Desktop/Python 2/Lektion 2/python2.txt", "w") as file: #w-läge för att skapa tom fil
    file.write("Write this example scentence in the empty file.\n")
    file.write("It is possible to write several lines.\n")
print("The content is now in the file python2.txt")

#again
with open("/Users/shanli/Desktop/Python 2/Lektion 2/python3.txt", "w") as file:
    file.write("Write this\n")
    file.write("Write this too.\n")
print("D for Done.")