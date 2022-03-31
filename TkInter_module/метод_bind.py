# bind - привязать
import tkinter as t
from tkinter import ttk



win = t.Tk()
win.geometry("500x500+1000+0")

style  = ttk.Style()
style.configure("TLabel", font = ("Times", 20), padding = 10, background = "cyan")

label = ttk.Label(text = "Click me!")
label.pack()

def click(event):
    style.configure("TLabel", background="red")


def leave(event):
    style.configure("TLabel", background="cyan")


label.bind("<Enter>",click)
label.bind("<Leave>",leave)


# <Return>
# <Button-1>
# <Double-Button-1>
win.mainloop()










