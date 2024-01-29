a = [int(input("-> ")) for i in range(int(input("Введите кол-во чисел последовательности:\nn = ")))]
k = int(input("Введите индекс:\nk = "))
c = int(input("Введите число, которое хотите добавить:\nc = "))
a.insert(k, c)
print(a)
