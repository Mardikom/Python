"""
ТИПЫ ИНФОРМАЦИИ:
1) строка - str - string
2) целое число - int - integer
3) нецелое число - float - floating number
4) список - list
5) словарь - dictionary
6) кортеж - tuple
"""
print(type("qwerty"))
print(type(5))
print(type(5.5))
#
# print('5+6 =',5+6)
# print("2" * 2)
#
# print(2 + 2)
# print(2 - 2)
# print(2 * 2) # умножение
# print(2 ** 3) # степень
# print(5 / 3) # деление
# print(5 // 3) # деление без остатка
# print(5 % 2) # остаток от деления

name = input("Ваше имя? ")
age = input("Ваш возраст? ")
city = input("В каком городе ты живешь? ")


print(f"Ваше имя: {name}")
print(f"Ваш город: {city}")
print(f"Ваш возраст: {age}")
# print("Вам будет " + str(int(age) + 10) + " через 10 лет")
print(f"Вам будет {int(age)+10} через 10 лет")


