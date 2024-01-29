import math
fi = int(input("Выбор фигуры\n1 - треугольник\n2 - прямоугольник\n3 - круг\n: "))
if fi == 1:
    a = float(input("Введите сторону a = "))
    b = float(input("Введите сторону b = "))
    c = float(input("Введите сторону c = "))
    p = (a + b + c) / 2
    s = math.sqrt((p*(p-a)*(p-b)*(p-c)))
    print(s)
if fi == 2:
    a = float(input("Введите сторону a = "))
    b = float(input("Введите сторону b = "))
    s = a * b
    print(s)
if fi == 3:
    r = float(input("Введите радиус r = "))
    s = math.pi*(r ** 2)
    print(s)
