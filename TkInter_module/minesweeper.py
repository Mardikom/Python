import tkinter as t
from random import randint
from tkinter import messagebox

win = t.Tk() 

win.configure(background="white")
win.title("MineSweeper")

def graphic_field():
    global label
    for x in range(10):
        for y in range(10):
            label = t.Label(width=6, height=3, bg="grey", relief= "ridge")
            label.bind("<Button-1>", click)
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

def click(event):
    clicked_label = event.widget
    info_grid = clicked_label.grid_info()
    row = info_grid["row"]
    column = info_grid["column"]
    print(row, column)
    clicked_label.config(background="red")
    print(big_spisok[row][column])
    if big_spisok[row][column] == 1:
        msbox = messagebox.askyesno("You lose", "YOU LOST!!!\nTry again?")
        clicked_label.config(bg="red", text="*")# п
    else:
        mines_around = 0
        clicked_label.config(bg="white")
        
        if row != 0:
            if big_spisok[row-1][column] == 1:
                mines_around +=1
        if column != 9 and row != 0:
            if big_spisok[row-1][column+1] == 1:
                mines_around +=1
        if column != 9:
            if big_spisok[row][column+1] == 1:
                mines_around +=1
        if column != 9 and row != 9:
            if big_spisok[row+1][column+1] == 1:
                mines_around +=1
        if row != 9:
            if big_spisok[row+1][column] == 1:
                mines_around +=1
        if row != 9 and column != 0:
            if big_spisok[row+1][column-1] == 1:
                mines_around +=1
        if column != 0:
            if big_spisok[row][column-1] == 1:
                mines_around +=1
        if column != 0 and row != 0:
            if big_spisok[row-1][column-1] == 1:
                mines_around +=1
            
        clicked_label.configure(text=mines_around)

start_game()


win.mainloop()


# ДЗ: условие для выигрыша.