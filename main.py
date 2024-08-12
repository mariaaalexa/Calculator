import tkinter as tk
from tkinter import ttk

def handle_button_click (clicked_button_text):
    current_text = result_var.get()

    if clicked_button_text == "=":
        try:
            expression - current_text.replace("÷", "/").replace("x", "*")
            result = eval(expression)

            if result.is_integer():
                result = int (result)

            result_var.set(result)

        except Exception as e:
             result_var.set("Error")
     
    elif clicked_button_text == "C":
        result_var.set ("")

    elif clicked_button_text == "%":
        try:
            current_number = float(current_text)
            result_var.set (current_number / 100)
        except ValueError:
            result_var.set("Error")

    elif clicked_button_text == "±":
        try:
            current_number = float(current_text)
            result_var.set (-current_number)
        except ValueError: 
            result_var.set ("Error")
    else:
        result_var.set(current_text + clicked_button_text)
            
root = tk.Tk() #de aici o sa porneasca toate obiectele ca niste ramuri
root.title("Calculator")

result_var = tk.StringVar()
#cream un text box de o linie pe care o putem edita
result_entry = ttk.Entry(root, textvariable=result_var, font=("Helvetica", 24), justify="right")
result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
]

root.mainloop()