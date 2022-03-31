from random import shuffle

while True:
    menu = input("1.Ознакомится с правилами.\n2.Начать игру.\n3.Остановить игру.\n")

    if menu == "1" :
        print("Загадывается 3-хзначное число без повторяющихся цифр и без нулей.\nПодсказки:\n\
    1) piсo - когда цифра есть в загаданном числе, но не стоит на том же месте\n\
    2) fermi - когда цифра есть в загаданном числе и стоит на том же месте\n\
    3) bagels - в нашем числе нет ни одной цифры из загаднного")
    elif menu == "2" :
        print("Вам загадали число\nДается 10 попыток\nПопробуйте его отгадать")
        spisok = ['1', '2', '3', '4', "5", "6", "7", "8", "9"]
        shuffle(spisok)
        random_number = "".join(spisok)[0:3]
        #print(random_number)
    elif menu == "3" :
        print("Игра остановлена.")
        break
        for x in range(10):
            hints = ""
            number = input("Ваше число: ")
            for i in number:
                if number.find(i) == random_number.find(i):
                    hints = hints + "Fermi "
                elif i in random_number:
                    hints = hints + "Piсo "
            if hints == "":
                print("Bagels")
            elif number == random_number:
                print("Вы угадали")
                break
            else:
                print(hints)
        if number != random_number:
            print("Вы проиграли")
            print(random_number)

# ДЗ: условия для проигрыша и выигрыша.






