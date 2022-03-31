import tkinter as t
from tkinter import ttk


win = t.Tk() 
win.geometry("512x512+800+50")
win.configure(background="cyan")
win.title("ОКНО")
win.resizable(width=False, height=False)


style = ttk.Style()


entry = ttk.Entry(font = ("times",20), justify = "right")
entry.pack()

def get_text():
    x = entry.get()
    entry.delete(0,"end") # удаление по индексам
    print(x)
    label.configure(text=x)
    style.configure("TLabel", background=x)

label = ttk.Label(text="          ")
label.pack()

button = ttk.Button(command = get_text, text="get text")
button.pack()

win.mainloop()


