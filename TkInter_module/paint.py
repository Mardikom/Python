import tkinter as t
from tkinter import ttk
from tkinter.colorchooser import askcolor



win = t.Tk()
win.geometry("1050x650+200+0")
win.title("Paint")

canvas = t.Canvas(relief="solid", bd = 1, width = 800, height=600, background="white")

scale = t.Scale(orient="vertical", length=200, from_= 1, to = 100)
scale.grid(row=0, column=2, rowspan=4, sticky="ns")

size = 1



color_chooser = "red"

def line(event):
    canvas.create_line(x,y,event.x,event.y, fill = color_chooser, width = scale.get(), capstyle= t.ROUND)
    first_click(event)

def first_click(event):
    global x,y
    x = event.x
    y = event.y


def choose_color():
    global color_chooser, color
    color_chooser = askcolor()[1]
    color = color_chooser


canvas.bind("<Button-1>", first_click)#для кисти
canvas.bind("<B1-Motion>", line)


def erase():
    global color_chooser
    color_chooser = "white"

def back(event):
    global color, color_chooser
    color_chooser = color

canvas.bind("<z>", back)

from PIL import ImageGrab

def getter():
    x=win.winfo_rootx() *2+canvas.winfo_x() * 2
    y=win.winfo_rooty()*2+canvas.winfo_y() * 2
    x1=x+canvas.winfo_width() * 2
    y1=y+canvas.winfo_height() * 2
    ImageGrab.grab().crop((x,y,x1,y1)).save("/Users/evgenijsalienko/Documents/Python/TKinter_module/image.png")



# def SaveImage(name):
#     from PIL import EpsImagePlugin, Image
#     import io
#     # EpsImagePlugin.gs_windows_binary = r'C:\Program Files\gspisok\gs9.53.3\bin\gswin64c.exe'
#     ps = canvas.postscript(colormode='color')
#     img = Image.open(io.BytesIO(ps.encode('utf-8')))
#     img.save(fp = "F:/"+name+".jpg")

choose_color_button = ttk.Button(text = "Цвет", command=choose_color)
eraser = ttk.Button(text = "Ластик", command=erase)
clean = ttk.Button(text = "Очистить", command = lambda : canvas.delete("all"))
save = ttk.Button(text = "Сохранить", command=getter)

canvas.grid(row=0, column=1, rowspan=4)
choose_color_button.grid(row=0, column = 0, sticky="ns")
eraser.grid(row=1, column = 0, sticky="ns")
clean.grid(row=2, column = 0, sticky="ns")
save.grid(row=3, column = 0, sticky="ns")


win.mainloop()

