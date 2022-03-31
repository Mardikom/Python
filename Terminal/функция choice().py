fromm random import choice 

spisok = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

color = "#"

for x in range(6):
    color += choice(spisok)

print(color)