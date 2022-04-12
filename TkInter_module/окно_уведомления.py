import tkinter as t
from tkinter import messagebox as mb

win = t.Tk() 

box = mb.askyesno(title="VICTORY", message="YOU WON!!!")
print(box)

if box:
    print("GAME STARTED AGAIN!!")
else:
    print("GAME OVER!!")


win.mainloop()

