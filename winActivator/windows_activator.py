import tkinter as t
from tkinter import Frame, ttk
from tkinter import messagebox as mb
import activation_script as act

win = t.Tk() 
win.title("Windows Activator")
win.geometry("300x150+600+50")
frame = t.Frame(win)
frame.pack()
#Label
selectYouWinVerLabel = ttk.Label(frame, text="Select your Windows version:")
selectYouWinVerLabel.pack()
#Buttons
win8Button = ttk.Button(frame, text="Windows 8")
win8Button.pack()
win8Button.config(width=17)
win81Button = ttk.Button(frame, text="Windows 8.1")
win81Button.pack()
win81Button.config(width=17)
win10ProButton = ttk.Button(frame, text="Windows 10 Pro / 11 Pro")
win10ProButton.pack()
win10ProButton.config(width=17)
win10LtscButton = ttk.Button(frame, text="Windows 10 LTSC")
win10LtscButton.pack()
win10LtscButton.config(width=17)
#Functions
def win8():
    act.win8activate()
def win81():
    act.win81activate()
def win10Pro():
    act.win10ProActivate()
def win10Ltsc():
    act.win10ltscActivate()



win.mainloop()