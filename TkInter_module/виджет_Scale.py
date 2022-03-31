import tkinter as t
from tkinter import Button, ttk

win = t.Tk() 
win.geometry("600x550+800+50")

scale2 = ttk.Scale(orient="horizontal", length=200, from_= 0, to = 10)
scale2.pack()

def get_value():
    print(scale2.get())

button = ttk.Button(text = "get value", command = get_value )
button.pack()
win.mainloop()



