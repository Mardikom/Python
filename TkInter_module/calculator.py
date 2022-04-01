import tkinter as t
from tkinter import ttk
import re

win = t.Tk() # создаем окно

win.title("Calculator")
win.resizable(width=False, height=False)

entry = ttk.Entry(font = ("helvetica",25), justify = "right")
entry.grid(row=0,column=0, columnspan=4,stick = "we")

entry.insert("end", 0)

style = ttk.Style()
style.configure("TButton",font = ("helvetica",18))

def add_digit(digit):
    if entry.get() == "0":
        entry.delete(0, "end")
    if entry.get()[-2:] in ["-0","+0","*0","/0"]:
        entry.delete(len(entry.get())-1, "end")
    entry.insert("end", digit)

def digit_button(digit):
    return ttk.Button(text = digit, command = lambda : add_digit(digit))

def add_operation(operation):
    if entry.get()[-1] in "+-*/.":
        entry.delete(len(entry.get())-1, "end")
    entry.insert("end", operation)


def operation_button(operation):
    return ttk.Button(text = operation, command = lambda : add_operation(operation))

def clear():
    entry.delete(0,"end")
    entry.insert("end", 0)


def calculate():
    storka = entry.get()
    entry.delete(0, "end")
    entry.insert(0, eval(storka))

def add_dot():
    storka = entry.get()
    if "." not in re.split("[-/*+]", storka)[-1] and storka[-1] not in "+-*/":
        entry.insert("end", ".")
        
def backspace():
    storka = entry.get()
    if storka != "0":
        entry.delete(len(storka)-1, "end")
    if entry.get() == "" :
        entry.insert("end", 0)

digit_button(1).grid(row = 4, column = 0)
digit_button(2).grid(row = 4, column = 1)
digit_button(3).grid(row = 4, column = 2)
digit_button(4).grid(row = 3, column = 0)
digit_button(5).grid(row = 3, column = 1)
digit_button(6).grid(row = 3, column = 2)
digit_button(7).grid(row = 2, column = 0)
digit_button(8).grid(row = 2, column = 1)
digit_button(9).grid(row = 2, column = 2)
digit_button(0).grid(row = 5, column = 0)

operation_button("+").grid(row = 2, column=3)
operation_button("-").grid(row = 3, column=3)
operation_button("/").grid(row = 4, column=3)
operation_button("*").grid(row = 5, column=3)


ttk.Button(text = "=", command=calculate).grid(row = 5, column = 2)
ttk.Button(text = "C", command=clear).grid(row = 6, column = 0, columnspan=2, sticky="we")
ttk.Button(text = ".", command=add_dot).grid(row = 5, column = 1)
ttk.Button(text = "CE", command=backspace).grid(row = 6, column = 2, columnspan=2, sticky="we")


win.mainloop()

