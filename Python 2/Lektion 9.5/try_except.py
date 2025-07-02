fruits = {
    "banana": 20,
    "apple": 15,
    "orange": 33,
    "mango": 12,
    "pear": 15
}

choose = input("Enter a fruit: ").lower() #.lower ska matcha key:sen i dicen (.capitalize ifall första bokstav ska va stor)
try:
    print(fruits[choose])
except KeyError:
    if choose == "all":
        print(fruits)
    else:
        print("Please try again.")
