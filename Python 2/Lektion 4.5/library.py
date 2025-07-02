#def main(): (flyttade ner till loopen)
library = {}
    #print("Library\n 1. Add book\n 2. Change info\n 3. Delete book\n 4. Show all books in library\n")
    #choice = input("Enter your action: ")

    #add book (title & writer)
def add_book(): #if choice == "1":
    book = input("Enter the title of the book: ")
    writer = input("Enter the writer of the book: ")
    library[book] = writer
    print(f"The {book} - {writer} is added to the library.")

#modify info
def modify_book(): #elif choice == "2":
    book = input("Enter the title of the book you want to modify: ")
    if book in library:
        update = input("Enter the update for the book: ")
        library[book] = update
        #adda to library (skriv rad)
        print(f"The {update} of the {book} has changed.")
    else:
        print(f"{book} does not exist in the library")

#del book from library
def del_book(): #elif choice == "3":
    book = input("Enter the title of the book you want to delete: ")
    del library[book]
    print(f"The {book} is deleted from the library\n")

#show all books
def show_all(): #elif choice == "4":
    print(f"All book {library}\n")

def main(): #
    while True:
        print("Library\n 1. Add book\n 2. Change info\n 3. Delete book\n 4. Show all books in library\n")
        action = input("Enter your action: ")

        if action == "1":
            add_book()

        elif action == "2":
            modify_book()

        elif action == "3":
            del_book()

        elif action == "4":
            show_all()

        else:
            print("Enter possible action please.")


main()