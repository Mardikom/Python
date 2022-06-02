import time
import tkinter as t
from tkinter import ttk
import requests

win = t.Tk() 
win.geometry("512x512+800+50")
win.title("WeatherAPP")
win.resizable(width=False, height=False)


def get_weather():
    global data

    date = time.strftime("%d %B, %I:%M %p")
    label_date.config(text = date)

    city = searchEntry.get()
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=1396c8d2a12422b51114f17c1e04512a').json()
    temp.config(text=data["main"]["temp"])

frame = ttk.Frame()
searchEntry = ttk.Entry(frame,font = ("helvetica",20), justify = "right")
searchEntry.grid(row=0, column=0, columnspan=2)
searchButton = ttk.Button(frame,text="Search", command=get_weather)
searchButton.grid(row=0, column=2)


frame2 = ttk.Frame()
label_date = ttk.Label(frame2)
label_date.grid(row=0, column=0)
temp = ttk.Label(frame2)    
temp.grid(row=0, column=1)

frame.pack()
frame2.pack()

win.mainloop()