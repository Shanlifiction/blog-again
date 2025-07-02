#Function that greets the user "Hello [name]! Welcome!"
#del 1 create
"""
def greet_function(name):
    message = ("Hello " + name + "! Welcome!")
    return message

#del 2 call 
result = greet_function("Anna")
print(result)

#or
#print(greet_funtion("Anna"))
"""


#Define a function that creates (input number into) list
#with loop and POW
#exempel: input [2, 3, 4] return [4, 9 16]
#my try
""" 
#del 1
import math #no need in this case

def create_list(x, y, z):
    for x in range:
        element_result = pow(x, y, z)
        return element_result

#del 2
print(create_list())
"""
#correct code for this methods (there are other ways)
#del 1
def List(lista):
    newList = []
    for element in lista: #lista ref to variable two lines above
        newElement = pow(element, 2) #element(s) (the listed numbers) ref to line above and saves looped ->element(s)<- one at a time
        newList.append(newElement) #adds to the end of list
    return newList

#del 2
print(List([2, 4, 5, 6, 7, 10]))

#Define a function that overwrites Ö with O and ö with o
#call "Ön nära Östermalm"
#my try
""""
#del 1
def Change(letter):
    for x in letter:
        if x == str.replace("ö", "o"):
            return letter
        if x == str.replace("Ö", "O"):
            return letter
"""
"""
def Change(text):
    var = ""
    for letter in text:
        if letter == "Ö":
            var = var + "O"
        elif letter == "ö":
            var = var + "o"
        else:
            var = var + letter
    return var
    
#del 2
print(Change("Ön nära östermalm"))
"""

def Change(text):
    var = ""
    for letter in text:
        if letter == "ö":
            var = var + "o"
        elif letter == "Ö":
            var = var + "O"
        else:
            var = var + letter
    return var

print(Change("Ön öster om Östermalm"))