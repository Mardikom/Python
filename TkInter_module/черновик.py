
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
'''            if row != 0:
                if big_spisok[row-1][column] == 1:
                    mines_around +=1
            if column != 9 and row != 0:
                if big_spisok[row-1][column+1] == 1:
                    mines_around +=1
            if column != 9:
                if big_spisok[row][column+1] == 1:
                    mines_around +=1
            if column != 9 and row != 9:
                if big_spisok[row+1][column+1] == 1:
                    mines_around +=1
            if row != 9:
                if big_spisok[row+1][column] == 1:
                    mines_around +=1
            if row != 9 and column != 0:
                if big_spisok[row+1][column-1] == 1:
                    mines_around +=1
            if column != 0:
                if big_spisok[row][column-1] == 1:
                    mines_around +=1
            if column != 0 and row != 0:
                if big_spisok[row-1][column-1] == 1:
                    mines_around +=1'''


print("asdjsagflkdfasgksdfg", end= "-")
print("rtyrtyrtyrtyrtyrty", end='-')
print("bcvvbnvbnbvnvbnbvn", end = '-')