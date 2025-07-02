import tkinter as tk

def button_click():
    etikett.config(text="Hi! You Changed the text.")

window = tk.Tk()
window.title("Welcome button window")

etikett = tk.Label(window, text="Push it.")
etikett.pack()

#text_var = tk.StringVar()
#text_var.set("Hello World!")
#label = tk.Label(window, textvariable=text_var, anchor=tk.CENTER, bg="lightblue", height=3, width=30, bd=3, font=("Arial", 16, "bold"), cursor="hand2", fg="green", padx=30, pady=90, justify=tk.CENTER, relief=tk.RAISED, underline=0, wraplength=250)
#label.pack(pady=80)

button = tk.Button(window, text="Simple Window", command=button_click)
button.pack()

window.mainloop()