a = [float(input("Введите число: ")) for i in range(int(input("Введите кол-во чисел последовательности: ")))]
print("Кол-во чисел: ", len(a))
sra = sum(a) / len(a)
print("Среднее арифметическое: ", sra)
print("Минимальное число: ", min(a))
print("Максимальное число: ", max(a))
