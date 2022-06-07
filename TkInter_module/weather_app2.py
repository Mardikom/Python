import time
import tkinter as t
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO
import base64

win = t.Tk() 
win.geometry("512x512+800+50")
win.title("WeatherAPP")
win.resizable(width=False, height=False)


def get_weather():
    global data, image2

    date = time.strftime("%d %B, %I:%M %p")
    label_date.config(text =date)

    city = searchEntry.get()
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=1396c8d2a12422b51114f17c1e04512a').json()
    
    get_image = requests.get(f'https://openweathermap.org/img/wn/{data["weather"][0]["icon"]}@2x.png', stream=True)
    image = base64.encodebytes(get_image.raw.read())
    image2= t.PhotoImage(data=image)
    imageLabel.config(image=image2)

    temp.config(text=f'Temperature: {data["main"]["temp"]}°C')
    feelsLike.config(text=f'Feels like: {data["main"]["feels_like"]}°C')
    sky.config(text=f'Weather: {data["weather"][0]["main"]}')
    countryAndCity.config(text=f'{data["name"]}, {data["sys"]["country"]}')

frame = ttk.Frame()
searchEntry = ttk.Entry(frame,font = ("helvetica",20), justify = "right")
searchEntry.grid(row=0, column=0, columnspan=2)
searchButton = ttk.Button(frame,text="Search", command=get_weather)
searchButton.grid(row=0, column=2)


frame2 = t.Frame()
label_date = t.Label(frame2, font = ("helvetica",15), fg="orange")
countryAndCity = t.Label(frame2, font = ("helvetica",20, 'bold'), )
imageLabel = t.Label(frame2)
temp = t.Label(frame2)    
feelsLike = t.Label(frame2)
sky = t.Label(frame2)  

label_date.grid(row=0, column=0, sticky="w")
countryAndCity.grid(row=1, column=0, sticky="w")
imageLabel.grid(row=2, column=0, sticky="w")
temp.grid(row=3, column=0,sticky="w")
feelsLike.grid(row=4, column=0, sticky="w")
sky.grid(row=5, column=0, sticky="w")

frame.pack()
frame2.pack()

win.mainloop()