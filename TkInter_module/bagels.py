import tkinter as t
from tkinter import HORIZONTAL, ttk
import random as r
from tkinter.constants import DISABLED, NORMAL


win = t.Tk() 
win.geometry("600x600+800+50")
win.configure(background="#F4A460")
win.title("Bagels")
#win.resizable(width=False, height=False)


def create_ran_num(N):
    spisok = ['1', '2', '3', '4', "5", "6", "7", "8", "9"]
    r.shuffle(spisok)
    return "".join(spisok)[0:N]


random_number = create_ran_num(3)

style = ttk.Style()
style.configure("TLabel", font = ("Trebuchet MS",20), padding = 10, background = "#F4A460")
style.configure("TButton", font = ("Trebuchet MS",20), padding = 10)
style.configure("R.TButton", font = ("Trebuchet MS",15), padding = 5)
counts = 10
clicks = 0

def check_number():
    global clicks,apply
    dificult_button.config(state=DISABLED)
    clicks = clicks + 1
    label_click_count.config(text="Попыток: " + str(clicks))
    number = entry.get()
    hints = ""
    for i in number:
        if number.find(i) == random_number.find(i):
            hints = hints + "Fermi "
        elif i in random_number:
                hints = hints + "Piсo "
    if hints == "":
        label2.config(text="Bagels")
    elif number == random_number:
        label2.config(text="Вы угадали")
        button1.config(state=DISABLED)
    else:
        label2.config(text=hints)
    if clicks == counts:
        label2.config(text="Вы проиграли\nЗагаданное число было "+random_number)
        button1.config(state=DISABLED)

def repeat():
    global clicks,random_number,apply
    dificult_button.config(state=NORMAL)
    random_number = create_ran_num(3)
    clicks = 0
    entry.delete(0,"end")
    label2.config(text="")
    button1.config(state=NORMAL)
    label_click_count.config(text="Попыток: 0")

def show_rules():
    win2= t.Tk() 
    win2.title("Правила")
    label_rules = ttk.Label(win2,text="Загадывается 3-хзначное число без повторяющихся цифр и без нулей.\n Подсказки:\n\
    1) piсo - когда цифра есть в загаданном числе, но не стоит на том же месте\n\
    2) fermi - когда цифра есть в загаданном числе и стоит на том же месте\n\
    3) bagels - в нашем числе нет ни одной цифры из загаднного")
    label_rules.pack()


def dificult_win():
    global scale, apply, win3
    win3 = t.Tk()
    win3.title("Сложность")
    label_dificult = ttk.Label(win3, text="Выберите сложность")
    apply = ttk.Button(win3,text="Принять", command=apply_dificult)
    scale = t.Scale(win3, orient=HORIZONTAL, from_=1, to=3)
    label_dificult.pack()
    scale.pack()
    apply.pack()

def apply_dificult():
    global counts, random_number
    lvl = scale.get()
    if lvl == 1:
        random_number = create_ran_num(3)
        counts = 10
        entry.config(width = 3)
    elif lvl == 2:
        random_number = create_ran_num(4)
        counts = 20
        entry.config(width = 4)
    elif lvl == 3:
        random_number = create_ran_num(5)
        counts = 25
        entry.config(width = 5)
    win3.destroy()


dificult_button = ttk.Button(style = "R.TButton", text="Сложность", command=dificult_win)
label_click_count = ttk.Label(text="Попыток: " + str(clicks))
label1 = ttk.Label(text="Угадайте число")
entry = ttk.Entry(font = ("Trebuchet MS",40), justify = "right", width = 3)
label2 = ttk.Label(text="")
button1 = ttk.Button(text="Принять ответ", command=check_number)
button2 = ttk.Button(text="Заново", command=repeat)
rules = ttk.Button(style = "R.TButton",text="Ознакомится с правилами", command=show_rules)

#label_click_count.pack(side="left", anchor="n")
label_click_count.place(x=10, y = 10)
label1.pack(pady = 70)
entry.pack(pady = 15)
label2.pack(pady = 15)
button1.pack(pady = 15)
button2.pack(pady = 15)
rules.place(x=310,y=10)
dificult_button.place(x=180, y=10)

win.mainloop()