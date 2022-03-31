import tkinter as t
from tkinter import ttk
import random as r
from tkinter.constants import DISABLED, NORMAL


random_num = r.randint(0,100)
win = t.Tk() 
win.geometry("600x512+800+50")
win.configure(background="cyan")
win.title("ОКНО")
win.resizable(width=False, height=False)




style = ttk.Style()
style.configure("TLabel", font = ("Arial",20), padding = 10, background = "Cyan")
style.configure("TButton", font = ("Arial",20), padding = 10)

clicks = 0
def check_number():
    global clicks
    clicks = clicks + 1
    label_click_count.config(text="Попыток: " + str(clicks))

    x = int(entry.get())

    if x == random_num:
        label2.config(text="Вы угадали")
        button1.config(state=DISABLED)
    elif x < random_num:
        label2.config(text="Ваше число меньше загаданого")
    elif x > random_num:
        label2.config(text="Ваше число больше загаданого")
    if clicks > 10:
        label2.config(text="Вы проиграли")
        button1.config(state=DISABLED)

def repeat():
    global clicks,random_num
    random_num = r.randint(0,100)
    print(random_num)
    clicks = 0
    entry.delete(0,"end")
    label2.config(text="")
    button1.config(state=NORMAL)



label_click_count = ttk.Label(text="Попыток: " + str(clicks))
label1 = ttk.Label(text="Угадайте число")
entry = ttk.Entry(font = ("arial",40), justify = "right", width = 3)
label2 = ttk.Label(text="")
button1 = ttk.Button(text="Принять ответ", command=check_number)
button2 = ttk.Button(text="Заново", command=repeat)




#label_click_count.pack(side="left", anchor="n")
label_click_count.place(x=10, y = 10)
label1.pack(pady = 15)
entry.pack(pady = 15)
label2.pack(pady = 15)
button1.pack(pady = 15)
button2.pack(pady = 15)







win.mainloop()
