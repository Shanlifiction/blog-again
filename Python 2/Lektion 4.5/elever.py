def main():
    students = {}

    while True:
        print("Buid a school class\n", "1: Add student\n", "2: Delete student\n", "3: Show all students\n", "4: Exit\n")
        choice = input("Enter your action: ")

        if choice == "1":
            name = input("Student name: ")
            age = input("Student age: ")
            students[name] = age #adderar namn och ålder i dictionary. Name key, age value
            print(f"Student {name} is added to the school class.")

        elif choice == "2":
            name = input("Enter the name of the student to delete name from class.")
            if name in students:
                del students[name]
                print(f"Student {name} is now deleted.")
            else:
                print(f"{name} does not exsist in this class.")
        
        elif choice == "3":
            if students:
                for name, age in students.items():
                    print(f"\t{name} - {age} years old\n")
            else:
                print("There are no students in the class.")

        elif choice == "4":
            break

        else:
            print("This is option is not availble. Try choosing an action from the startmeny again.\n")


main()