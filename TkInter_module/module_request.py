
# https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=1396c8d2a12422b51114f17c1e04512a

import requests

data = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=1396c8d2a12422b51114f17c1e04512a').json()

for x in data:
    print(x,":", data[x])


# ДЗ: Визуализировать данные о погоде в интерфейсе

