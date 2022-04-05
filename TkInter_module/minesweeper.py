import tkinter as t
from tkinter import ttk
from random import randint

win = t.Tk() 

win.configure(background="white")
win.title("ОКНО")

def graphic_field():
    for x in range(10):
        for y in range(10):
            label = t.Label(width=6, height=3, bg="green", relief= "ridge")
            label.grid(row=x, column=y)

def digit_field():  
    global big_spisok
    big_spisok = []
    for x in range(10):
        spisok = []
        for x in range(10):
            if randint(0,100) < 25:
                spisok.append(1)
            else:
                spisok.append(0)
        big_spisok.append(spisok)

def print_digit_field():
    for y in big_spisok:
        print(y)


def start_game():
    digit_field()
    print_digit_field()
    graphic_field()



start_game()


win.mainloop()

#ДЗ: по нажатию на любую ячейку она меняет цвет на синий