number1 = int(input("Первое число: "))
operator = input("Знак вычесления: ")
number2 = int(input("Второе число: "))


if operator == "+":
    print(f"Результат: {number1 + number2}" )
if operator == "-":
    print(f"Результат: {number1 - number2}")
if operator == ":":
    print(f"Результат: {number1 / number2}" )
if operator == "*":
    print(f"Результат: {number1 * number2}" )
if operator == "^":
    print(f"Результат: {number1 ** number2}" )
if operator == "%":
    print(f"Результат: {number1 % number2}" )




