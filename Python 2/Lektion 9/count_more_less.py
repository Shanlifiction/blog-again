import tkinter as tk
#from tkinter import ttk

root = tk.Tk()
root.title("Click and Count")
root.geometry("800x600")

"""
def clicked():
    global count
    count = count + 1
    label.configure(text=f"Clicked {count} times!")
"""

def increase_click():
    current_value = int(label["text"])
    label.config(text=str(current_value + 1))

def decrease_click():
    current_value = int(label["text"])
    label.config(text=str(current_value - 1)) 

label = tk.Label(root, text="0", font=("arial", 24))
label.pack(pady=20)

button1 = tk.Button(root, text="More", command=increase_click)
button1.pack(side="left")
button2 = tk.Button(root, text="Less", command=decrease_click)
button2.pack(side="right")

root.mainloop()