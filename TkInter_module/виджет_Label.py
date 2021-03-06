import tkinter as t
from tkinter import ttk
from tkinter import font
from random import choice
import requests
import base64



win = t.Tk() 
win.geometry("512x512+800+50")
win.configure(background="cyan")
win.title("ОКНО")
win.resizable(width=False, height=False)

get_image = requests.get(f'https://openweathermap.org/img/wn/02n@2x.png', stream=True)
image = base64.encodebytes(get_image.raw.read())
image2= t.PhotoImage(data=image)


style = ttk.Style()
style.configure("TLabel", font = ("times",20), padding = 10, background = "red")

style.configure("TButton", font = ("times",20), padding = 10, background = "blue")

label = ttk.Label(text="Label")
label.config(image=image2)
label.pack()

spisok = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

def changecolour():
    global color
    color = "#"
    for x in range(6):
        color += choice(spisok)
    print(color)
    label.config(text=color)
    style.configure("TLabel", background=color)


button = ttk.Button(command=changecolour, text="button")
button.pack()
win.mainloop()