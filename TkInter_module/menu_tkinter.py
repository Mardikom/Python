import tkinter as t
from random import randint
from tkinter import messagebox

win = t.Tk() 
win.geometry("300x300")

menu = t.Menu(win)



mode_menu = t.Menu(menu)
fixed_menu = t.Menu(menu)

menu.add_cascade(label="Mode", menu=mode_menu)



mode_menu.add_command(label="Hide", command = None)
mode_menu.add_command(label="Not hide", command = None)
mode_menu.add_command(label="Minimal", command = None)
mode_menu.add_command(label="Fixed", command = None)

#fixed_menu.add_command(label="fixed", command = None)

win.config(menu = menu)
win.mainloop()


#дз перенести в cpu util 2