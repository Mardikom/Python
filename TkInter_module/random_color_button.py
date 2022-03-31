import tkinter as t
from tkinter import ttk
from random import choice

win = t.Tk() 
win.geometry("512x512+800+50")
win.title("ОКНО")
win.resizable(width=False, height=False)


spisok = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

def random_colour():
    global color
    color = "#"
    for x in range(6):
        color += choice(spisok)
    print(color)
    button.config(text=color)
    style.configure("TButton", foreground=color,font=("arial",20), padding = 10)#стиль кнопки

style = ttk.Style()

button = ttk.Button(command=random_colour)
button.pack(side = "left", anchor = "e")

random_colour()

win.mainloop()
# place, grid, pack