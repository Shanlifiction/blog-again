#definera en funktion som beräknar arean av en triangel. Ta in "bas" och "höjd" (m) som parametrar.
#Använd funktionen för att printa arean av triangeln med basen 5m och hgöjd 7m.
#arean av triangeln ör: bas * höj/2
def triangelArea (bas, höjd): #skicka namn på (tomma) värden
    area = bas * höjd/2 #innanför funtionen kan beräkningen göras, där även variabeln deklareras
    return area
print(triangelArea(5,7),"kvadratmeter") #värden anges och anropas

#samma fast med cirkel och exakt värde på pi
import math
def cirkelArea (radie):
    area = math.pi * pow (radie,2) #pow gör det möjligt att höja upp till, radie  är (bas), 2 är (upphöjt till)
    return area
print(cirkelArea(3), "kvadratmeter") #varför en trea???


#övning "printa max talet"
nums = [3, 55, -5]
print(max(nums))

#samma print fast med hjälp av en funktion
def nums (tal1, tal2, tal3):
    return max ([tal1, tal2, tal3]) #klammar behövs ej
print (nums(3, 55, -5))

#valfri datatyp
def my_function(food):
    for x in food:
        print(x)
    return x
    
my_function("Cucumber") #endast första bokstaven kmr tbks ifall return är tab in (under print)


#anropa lista 
def fruit_list(fruits):
    for x in fruits:
        print(x)
    return x #behövs ej eftersom funtionens uppgift är att skriva ut en lista

fruit_list (["Banana", "Apple", "Orange", "Cherry"])

#funtion med två ord
def long_word(word1, word2):
    if len(word1) > len(word2):
        return word1
    else:
        return word2
print(long_word("bok", "linjal"))

def longest_word(words):
    for x in words:
        print(x)
        return x
print(longest_word(["book", "pen"]))

#skapa lista som adderar talens värden
def add_hundreds(list):
    total = sum(list)
    endtotal = total + 100
    return endtotal
print(add_hundreds([100,300,400,3]))

def add_hund(list):
    total = 0
    for element in list:
        total = total + element
    total = total + 100
    return total
print(add_hund([100,300,400,3]))