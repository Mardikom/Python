# ДЗ: нужно спросить через input любую строку и после этого должна распечатываться средняя
# буква из строки, но если в строке четное количество символов, то распечатать 2 средние буквы

txt = input("Введите текст: ")

length = len(txt)
if length % 2 == 1:
    print(txt[length//2])
else:
    print(txt[length//2 - 1:length//2 + 1])



