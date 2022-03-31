import tkinter as t
from tkinter import ttk
from tkinter import font

win = t.Tk() # создаем окно
win.geometry("512x512+800+50")
win.title("ОКНО")
# win.iconbitmap()
win.resizable(width=False, height=False)

clicks = 0
def clicker(): #функция кнопки
    global clicks
    clicks = clicks + 1
    button.config(text=clicks)
    # style.configure("TButton", background="red")

style = ttk.Style() #стиль кнопки
style.configure("TButton", background="#00D9FF",font=("arial",20, "bold italic"), padding = 10)#стиль кнопки

button = ttk.Button(text="click me", state = "disabled",command = clicker)
button.pack()


for x in font.families():
    print(x)

win.mainloop() # запускаем основной цикл окна





