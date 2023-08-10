#  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не 
# настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

str_1 = input("Введите фразу: ")
vowels = "аеёиоуыэюя"
lst_1 = []
str_1 = str_1.split()

for word in str_1:
     sum = 0
     for i in word:
         if i in vowels:
             sum += 1
     lst_1.append(sum)
    
lst_1 = set(lst_1)   

if len(lst_1) > 1:
     print("Пам парам")
else:
     print("Парам-пам-пам")



# Можно сделать тоже самое и через функцию:

def rithm_detection(str_1):
    lst_1 = []
    str_1 = str_1.split()

    for word in str_1:
        sum = 0
        for i in word:
            if i in vowels:
             sum += 1
        lst_1.append(sum)
    
    lst_1 = set(lst_1)   

    if len(lst_1) > 1:
        return True
    

    
str_1 = input("Введите фразу: ")
vowels = "аеёиоуыэюя"

if rithm_detection(str_1) == True:
   print("Пам парам")
else:
    print("Парам-пам-пам")


# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, 
# у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
     for i in a:
         print(*[f"{x:>3}" for x in i])


print_operation_table(lambda x, y: x * y)

# Тоже самое, но в немного развернутом виде...

def print_operation_table(operation, num_rows=6, num_columns=6):
     for i in range(1, num_rows + 1):
         a = []
         for j in range(1, num_columns + 1):
             a.append(str(operation(i, j)))
         print(*[f"{x:>3}" for x in a])

print() 
print_operation_table(lambda x, y: x * y)