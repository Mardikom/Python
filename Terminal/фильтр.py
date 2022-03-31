'''
def фильтр(список):
    strings = []
    for x in список:
        if type(x) == str:
            strings.append(x)
    return strings
'''

# строки = ["asd",'cvb',4,31,'asdas']
# print(фильтр(строки))
# print(len(строки))


числа = [1, 34, 4, 5, 7]


def четные_числа(список):
    spisok = []
    for x in список:
        if x % 2 == 0:
            spisok.append(x)
    return spisok


print(четные_числа(числа))

