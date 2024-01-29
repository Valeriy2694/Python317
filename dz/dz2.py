n = int(input("Введите количество копеек: "))
if 1 <= n <= 99:
    if n == 11 or n == 12 or n == 13 or n == 14:
        print(n, "копеек")
    else:
        if n % 10 == 1:
            print(n, "копейка")
        if n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
            print(n, "копейки")
        if 5 <= n % 10 <= 9 or n % 10 == 0:
            print(n, "копеек")
else:
    print("Ошибка ввода данных")
