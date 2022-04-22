import tkinter as t
from random import randint
from tkinter import messagebox

win = t.Tk() 
win.geometry("300x300")

menu = t.Menu()

menubar = t.Menu(menu)

menu.add_cascade(label="Options", menu = menubar)

menubar.add_command(label="Change LVL", command = None)
menubar.add_command(label="start again", command = None)
menubar.add_command(label="Exit", command = None)

win.config(menu = menu)
win.mainloop()