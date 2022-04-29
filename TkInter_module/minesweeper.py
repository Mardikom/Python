import tkinter as t
from random import randint
from tkinter import messagebox, ttk
#-alpha, -fullscreen, -modified, -notify, -titlepath, -topmost, -transparent, or -type
win = t.Tk() 
win.attributes("-titlepath", '/Applications/Visual\ Studio\ Code.app/Contents/Resources/Code.icns')
squares = 10

win.configure(background="white")
win.title("MineSweeper")

flags = 0
clicks = 0

def menubar():
    def change_lvl():
        global combobox
        win_level = t.Toplevel()
        combobox = ttk.Combobox(win_level, values = ("Easy (10x10)", "Medium (15x15)", "Hard (20x20)"), state = 'readonly')
        apply = ttk.Button(win_level, text="Apply", command=start_game)
        combobox.current(0)
        combobox.bind("<<ComboboxSelected>>", select_level)
        combobox.pack()
        apply.pack()
    menu = t.Menu()
    menubar = t.Menu(menu)
    menu.add_cascade(label="Options", menu = menubar)
    menubar.add_command(label="Change LVL", command = change_lvl)
    menubar.add_command(label="Start again", command = start_game)
    menubar.add_command(label="Exit", command = win.destroy)
    win.configure(menu = menu)

def select_level(event):
    global squares
    squares = 5 * combobox.current() + 10

def graphic_field():
    global label, squares
    for x in range(squares):
        for y in range(squares):
            label = t.Label(width=4, height=2, bg="grey", relief= "ridge")
            label.bind("<Button-1>", click)
            label.bind("<Button-2>", add_flag)
            label.grid(row=x, column=y)

def add_flag(event):
    global flags
    clicked_label = event.widget
    if clicked_label["bg"] == "yellow":
        flags -= 1
        clicked_label.config(bg="grey")
    elif clicked_label["bg"] == "grey" and flags < bombs:
        flags += 1
        clicked_label.config(bg="yellow")
    print("flags",flags)
        
def digit_field():  
    global big_spisok, squares
    big_spisok = []
    for x in range(0,squares+2):
        spisok = []
        for x in range(0,squares+2):
            spisok.append(0)
        big_spisok.append(spisok)


    for x in range(1,squares+1):
        for y in range(1,squares+1):
            if randint(0,100) < 25:
                big_spisok[x][y] = 1

def print_digit_field():
    for x in range(1,squares+1):
        for y in range(1,squares+1):
            if y == squares:
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
    labels_destroy()
    menubar()    
    digit_field()
    print_digit_field()
    graphic_field()

def click(event):
    global clicks, bombs
    print(clicks)
    clicked_label = event.widget
    if clicked_label['bg'] == "grey":
        info_grid = clicked_label.grid_info()
        row = info_grid["row"] + 1
        column = info_grid["column"] + 1
        if clicks == 0:
            first_click(row = row,column = column)
            bombs = all_mines_count(big_spisok)
        if big_spisok[row][column] == 1:
            clicked_label.config(bg="red", text="*")
            endgame(victory = False)
        else:
            mines_around = 0
            clicks += 1
            if clicks == squares*squares - bombs:
                endgame()
            clicked_label.config(bg="white")
            for row_shift in [-1, 0, 1]:
                for col_shift in [-1, 0, 1]:
                    if big_spisok[row + row_shift][column + col_shift] == 1:
                        mines_around += 1
            clicked_label.configure(text=mines_around)

def all_mines_count(field):
    count = 0
    for x in field:
        for y in x:
            if y == 1:
                count += 1
    print(count)
    return count
            
def first_click(row, column):
    big_spisok[row][column] = 0
    for row_shift in [-1, 0, 1]:
        for col_shift in [-1, 0, 1]:
            big_spisok[row + row_shift][column + col_shift] = 0
    
start_game()
win.mainloop()


# ДЗ: Создать функцию create menu