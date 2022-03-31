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

# columnspan - совмещение колонок
# rowspan - совмещение рядов
# stick - north(север), south(юг), west(запад),east(восток)

button1.grid(row=0, column = 0)
button2.grid(row=0, column = 1)
button3.grid(row=1, column = 0)
button4.grid(row=1, column = 1)
button5.grid(row=2, column = 0, columnspan=2, stick = "we")
button6.grid(row=0, column = 2, rowspan=3, sticky="ns")



win.mainloop()



