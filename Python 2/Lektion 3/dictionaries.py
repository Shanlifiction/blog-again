person = {"name": "Christian", "age": 25}
print(person["name"]) #när keys hanteras används square brackets

person = {
    "first_name": "Lisa", #key:value
    "last_name": "Svensson",
    "age": 32
}
choice = input("Choose an attribute (first_name, last_name or age): ")
try:
    print(person[choice]) #print(dictionaryName[(indirekt)key/key-chioce])
except KeyError:
    print("ERROR: The attribute does not exist.")