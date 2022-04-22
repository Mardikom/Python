import tkinter as t
from random import randint
from tkinter import messagebox

win = t.Tk() 

menu = t.Menu()

menubar = t.Menu(menu)

menu.add_cascade(label="Options", menu = menubar)

menubar.add_command(label="Change LVL", command = None)
menubar.add_command(label="start again", command = None)
menubar.add_command(label="Exit", command = None)

win.configure(menu = menu)
win.configure(background="white")

win.title("MineSweeper")
win.resizable(False, False)

def graphic_field():
    global label
    for x in range(10):
        for y in range(10):
            label = t.Label(width=6, height=3, bg="grey", relief= "ridge")
            label.bind("<Button-1>", click)
            label.bind("<Button-2>", add_flag)
            label.grid(row=x, column=y)

    
def add_flag(event):
    clicked_label = event.widget
    if clicked_label["bg"] == "yellow":
        clicked_label.config(bg="grey")
    elif clicked_label["bg"] == "grey":
        clicked_label.config(bg="yellow")


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
    for x in range(1,11):
        for y in range(1,11):
            if y == 10:
                print(big_spisok[x][y], end="\n")
            else:
                print(big_spisok[x][y], end=" ")


def endgame(victory = True):
    global clicks
    message = {True: "YOU WIN!!!", False : "YOU LOST!!!"}
    if messagebox.askyesno("", f"{message[victory]}\nTry again?"):
        clicks = 0
        start_game()
    else:
        win.destroy()

            
def labels_destroy():
    for x in win.winfo_children():
        x.destroy()

def start_game():
    labels_destroy
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
        if clicks == 0:
            first_click(row = row,column = column)
        if big_spisok[row][column] == 1:
            clicked_label.config(bg="red", text="*")
            endgame(victory = False)
        else:
            mines_around = 0
            clicks += 1
            if clicks == 100 - bombs:
                endgame()
            clicked_label.config(bg="white")
            for row_shift in [-1, 0, 1]:
                for col_shift in [-1, 0, 1]:
                    if big_spisok[row + row_shift][column + col_shift] == 1:
                        mines_around += 1
            clicked_label.configure(text=mines_around)
            
def first_click(row, column):
    big_spisok[row][column] = 0
    for row_shift in [-1, 0, 1]:
        for col_shift in [-1, 0, 1]:
            big_spisok[row + row_shift][column + col_shift] = 0
                
start_game()
win.mainloop()


