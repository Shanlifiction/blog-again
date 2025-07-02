#används för att hantera oväntade eller felaktiga händelser i programmet
#placerar error inom kodblock
"""
def int_num():
    try:
        num = int(input("Write a number: "))
        print("You wrote: ", num)
    except:
        print("Error. You must write a ...")

int_num()
"""

#again
"""
def int_nums():
    try:
        tal = int(input("Skriv tal: "))
        print("Du skrev: ", tal)
    except:
        print("Error. Skriv ett heltal.")

int_nums()
"""

#finns flera exception-typer
#except ValueError:
    #print("Felaktigt värde! Var god skriv heltal.")
#except ZeroDivisionError:
    #print("Division med 0 är inte tillåtet inom matematik.")
#except Exception "as e:"
    #print("Ett oväntat fel uppstod.", e)
#else:
    #print("Inga fel uppstod. Resultatet av 10 delat med", num, "är:", result)
#finally:
    #print("Programmet är klart.")


#r innan sökväg står för raw-string
"""
try:
    with open(r"sökväg", "r"):
        content = file.read()
        print(content)
except Exception as e:
    print("Oväntat fel.")
"""

#Skriv ett program som ber användaren om att mata in ett tal. Använd try/except
#giltigt tal
#skriv ut talet i kvadrerat
#om ej giltig, skriv felmed.


#gissade 
"""
try:
    number = int(input)
    print()
except Exception as e:
    print("")
"""
"""
#import math #behövs inte
try:
    number = float(input("Skriv heltal: "))
    print(pow(number, 2))
except ValueError:
    print("Felaktig inmatning. Skriv ett tal.")
"""

try:
    num1 = float(input("Skriv in ett tal nummer 1: "))
    num2 = float(input("Skriv in tal nummer 2: "))
    #går att skriva utan "else:" och result line här
    print("Du knappade in:", num1, "och ", num2)
except ValueError:
    print("Felaktig inmatning! Var god ange numeriska värden för talet.")
except ZeroDivisionError:
    print("Du kan inte skriva 0.")
except Exception as e:
    print("Nu blev något knas. Ett oväntat knas.", e) #i detta fall är ValueError det samma så Exception as e nedprioriteras
else:
    result = (num1 + num2) / 2 #parantes för att prioritera multiplikation
    #print("Dina två tal delat på 2 är: ", (num1 + num2) / 2) #går att skriva ut result utan result variabel
    print("Dina två tal delat på 2 är: ", result)
