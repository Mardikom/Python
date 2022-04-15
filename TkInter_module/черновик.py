
from random import randint

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
            
for x in big_spisok:
    print(x)
