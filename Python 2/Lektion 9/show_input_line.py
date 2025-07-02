import tkinter as tk
from tkinter import messagebox

root = tk.Tk() 
root.title("Welcome")
root.geometry("800x600") #window bredd800 & höjd600

def input_line():
    #line.config(f"Input: {line.get}")
    user_input = line.get()
    messagebox.showinfo("Message", f"Input message: {user_input}") #positional args
    #messagebox.showinfo(f"Input: {line.get}")

line = tk.Entry(root, width=30)
line.pack(pady=5) 
line.focus() #placerar markören direkt i fönstret

button = tk.Button(root, text=("Show input message"), command=input_line)
button.pack(pady=5)


root.mainloop()

