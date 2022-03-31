import tkinter as t
from tkinter import ttk


win = t.Tk()
win.geometry("800x500+600+0")
style  = ttk.Style()
style.configure("TButton", font = ("Times", 20), padding = 10)

button1 = ttk.Button(text = "button 1")
button2 = ttk.Button(text = "button 2")
button3 = ttk.Button(text = "button 3")
button4 = ttk.Button(text = "button 4")
button5 = ttk.Button(text = "button 5")
button6 = ttk.Button(text = "button 6")
button7 = ttk.Button(text = "button 7")
button8 = ttk.Button(text = "button 8")
button9 = ttk.Button(text = "button 9")
button10 = ttk.Button(text = "button 10")
button11 = ttk.Button(text = "button 11")


button1.grid(row=0, column = 0, columnspan = 2, stick = "we")
button2.grid(row=0, column = 2, rowspan=2, stick = "ns")
button3.grid(row=1, column = 0)
button4.grid(row=1, column = 1)
button5.grid(row=0, column = 3, rowspan=4, sticky="ns") 
button6.grid(row=2, column = 0, columnspan=3, stick="we")
button7.grid(row=3, column = 0, rowspan=2, sticky="ns")
button8.grid(row=3, column = 1, columnspan=2, sticky="we")
button9.grid(row=4, column = 1, columnspan=3, sticky="we")
button10.grid(row=5, column = 0, columnspan=4, sticky="we")
button11.grid(row=0, column = 4, rowspan=6, sticky="ns")




win.mainloop()

#  ДЗ: Создать лэйбл.
#  По нажатию лкм лэйбл должен менять цвет на рандомный.
#  По двойному нажатию лкм - менять шрифт на рандомный.


