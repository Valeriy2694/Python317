from math import pi


def rectangle():
    a = int(input("Сторона a: "))
    b = int(input("Сторона b: "))
    return a * b


def triangle():
    a = int(input("Основание: "))
    b = int(input("Высоту: "))
    return (a * b) / 2


def circle():
    r = int(input("Радиус: "))
    return pi * r ** 2


figure = int(input("Выберите фигуру\n1 - прямоугольник, 2 - треугольник, 3 - круг: "))
if figure == 1:
    print("Площадь: ", rectangle())
elif figure == 2:
    print("Площадь: ", triangle())
elif figure == 3:
    print("Площадь: ", round(circle(), 2))
else:
    print("Ошибка ввода данных!")
