
import tkinter as t
from tkinter import ttk


win = t.Tk()
win.geometry("500x300+1000+50")


combobox = ttk.Combobox(values = ("easy(10x10)", "medium(15x15)", "hard(20x20)"), state = 'readonly')
combobox.current(0)



def select_option(event):
    squares = 5 * combobox.current() + 10



combobox.bind("<<ComboboxSelected>>", select_option)
combobox.pack()





win.mainloop()