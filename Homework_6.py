# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.



a1 = int(input("Введите первый элемент списка: "))
dif = int(input("Введите разность: "))
size_list_1 = int(input("Введите размер списка: "))
list_1 = []
for i in range(size_list_1):
    a = a1 + (i - 1) * dif
    list_1.append(a)
for item in list_1:
    print(item)



# Определить индексы элементов массива (списка), значения
# которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


from random import randint
size_list_1 = int(input("Введите размер массива: "))
max_1 = int(input("Введите максимальное значение: "))
min_1 = int(input("Введите минимальное значение: "))
list_1 = [randint(1,20) for i in range(size_list_1)]
print(list_1)
list_2 = []
for i in range (size_list_1):
    if list_1[i] >= min_1 and list_1[i] < max_1:
        list_2.append(i)
print(list_2)

# Можно не объявлять еще один список, а просто вывести индексы, что тоже соответствует условиям задачи

from random import randint
size_list_1 = int(input("Введите размер массива: "))
max_1 = int(input("Введите максимальное значение: "))
min_1 = int(input("Введите минимальное значение: "))
list_1 = [randint(1,20) for i in range(size_list_1)]
print(list_1)
for i in range (size_list_1):
    if list_1[i] >= min_1 and list_1[i] < max_1:
        print(i, end = " ")
