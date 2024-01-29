n = int(input("Введите кол-во символов: "))
sim = input("Укажите тип символа: ")
lin = int(input("Ориентация линии ( 0 - горизонтальная, 1 - вертикальная): "))
if lin == 0 or lin == 1:
    if lin == 0:
        print(sim * n)
    if lin == 1:
        i = 0
        while i < n:
            print(sim)
            i += 1
else:
    print("Некорректное значение ориентации линии")
