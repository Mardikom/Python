# bind - привязать
import tkinter as t
from tkinter import ttk



win = t.Tk()
win.geometry("500x500+500+0")

style  = ttk.Style()
style.configure("TLabel", font = ("Times", 20), padding = 10, background = "cyan")

label = ttk.Label(text = "Click me!")
label.pack()

def click(event):
    label.config(background="red")
    # label.config(bg = "red")

def leave(event):
    style.configure("TLabel", background="cyan")


label.bind("<Button-1>", click)
label.bind("<Leave>",leave)


# <Return>
# <Button-1>
# <Double-Button-1>
win.mainloop()










