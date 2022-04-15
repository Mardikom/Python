from operator import contains
import tkinter as t
from random import randint
from tkinter import messagebox

win = t.Tk() 

win.configure(background="white")
win.title("MineSweeper")
win.resizable(False, False)

def graphic_field():
    global label
    for x in range(10):
        for y in range(10):
            label = t.Label(width=6, height=3, bg="grey", relief= "ridge")
            label.bind("<Button-1>", click)
            label.grid(row=x, column=y)

bombs = 0

def digit_field():  
    global big_spisok, bombs
    big_spisok = []
    for x in range(0,12):
        spisok = []
        for x in range(0,12):
            spisok.append(0)
        big_spisok.append(spisok)


    for x in range(1,11):
        for y in range(1,11):
            if randint(0,100) < 25:
                big_spisok[x][y] = 1

def print_digit_field():
    for y in big_spisok:
        print(y)
    
def won():
    if clicks == 100-bombs:
        if messagebox.askyesno("You win", "YOU WIN!!!\nTry again?"):
            start_game()
        else:
            win.destroy()

def label_destroy():
    for x in win.winfo_children():
        x.destroy()

def start_game():
    label_destroy
    digit_field()
    print_digit_field()
    graphic_field()
    
clicks = 0

def click(event):
    global clicks
    print(clicks)
    clicked_label = event.widget
    if clicked_label['bg'] == "grey":
        info_grid = clicked_label.grid_info()
        row = info_grid["row"] + 1
        column = info_grid["column"] + 1
        if big_spisok[row][column] == 1:
            clicked_label.config(bg="red", text="*")
            if messagebox.askyesno("You win", "YOU LOST!!!\nTry again?"):
                start_game()
            else:
                win.destroy()
        else:
            mines_around = 0
            clicks += 1
            won()
            clicked_label.config(bg="white")
            

'''            if row != 0:
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
                    mines_around +=1'''
                
            clicked_label.configure(text=mines_around)

start_game()


win.mainloop()


# ДЗ: условие для выигрыша.