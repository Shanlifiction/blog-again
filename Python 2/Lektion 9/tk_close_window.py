import tkinter as tk

def close_window():
    root.destroy()

root = tk.Tk() #skapa objekt i Tk-klassen (objekt = bibliotek.Klassnamn())
root.title("Simple Window")

button = tk.Button(root, text="Close Window", command=close_window) #skapa ytterligare ett objekt i Button-klassen (med deets)

button.pack(pady=250) #"packa"/placera (som padding i CSS typ?)
root.mainloop() #starta huvudloopen för att köra applikationen