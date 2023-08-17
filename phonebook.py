# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

#  Печать данных
def show_data(filename):
    print("\nПП | ФИО | Телефон| Комментарии")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")

# Записывает информацию в файл
def export_data(filename):
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(filename, "a", encoding="utf-8") as data: 
        fio = input("Введите ФИО: ")
        phone_number = input("Введите номер телефона: ")
        addition = input("Введите комментарий: ")
        data.write(f"{num} |{fio} | {phone_number} | {addition}\n")
        print(f"Добавлена запись : {num} | {fio} | {phone_number} | {addition}\n")

# Изменяет информацию из файла
def edit_data(filename):
    print("\nПП | ФИО | Телефон | Комментарии")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    addition = input("Введите комментарии: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    if len(addition) == 0:
        addition = elements[3]
    edited_line = f"{num} | {fio} | {phone} | {addition}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

# Удаляет информацию из файла
def delete_data(filename):
    print("\nПП | ФИО | Телефон | Комментарии")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))


# Поиск контакта
def find_data(filename):
    with open(filename, "r", encoding = "utf-8") as data:
        tel_book = data.readlines()
        name = input("Введите параметр для поиска (ФИО, номер телефона, комментарий): ")
        print("\nПП | ФИО | Телефон | Комментарии")
        for i in range(len(tel_book)):
            if name in tel_book[i]:
                print(tel_book[i])
       

def main():
    my_choice = -1
    file_tel = "phone.txt"

    # Создает файл если его нет в папке
    with open(file_tel, "a", encoding="utf-8") as file:
         file.write("")

    while my_choice != 0:
        print("Выберите одно из действий:")
        print("1 - Вывести список контактов на экран")
        print("2 - Добавить новый контакт")
        print("3 - Изменить контакт")
        print("4 - Удалить контакт")
        print("5 - Найти контакт")
        print("0 - Выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            show_data(file_tel)
        elif action == 2:
            export_data(file_tel)
        elif action == 3:
            edit_data(file_tel)
        elif action == 4:
            delete_data(file_tel)
        elif action == 5:
            find_data(file_tel)
        else:
            my_choice = 0

    print("До свидания")

if __name__ == "__main__":
    main()