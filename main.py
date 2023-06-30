# ^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!*@#$%^&+=]).*$
# ^[0-9a-zA-Z]+[./+_-]{0,1}[0-9a-zA-Z]+[@][a-zA-Z0-9]+[.][a-zA-Z]{2,}$
# t_e@s.com
# ^[+]{0,1}[380][0-9]{7}$
# "^[a-zA-ZА-Яа-яёЁЇїІіЄєҐґ]+$"

###
# r (Read). Файл открывается для чтения. Если файл не найден, то генерируется исключение FileNotFoundError
#
# w (Write). Файл открывается для записи. Если файл отсутствует, то он создается. Если подобный файл уже есть,
# то он создается заново, и соответственно старые данные в нем стираются.
#
# a (Append). Файл открывается для дозаписи. Если файл отсутствует, то он создается.
# Если подобный файл уже есть, то данные записываются в его конец.
#
# b (Binary). Используется для работы с бинарными файлами. Применяется вместе с другими режимами - w или r.

# # v1
# try:
#     my_file = open("hello.txt", "w")
#     try:
#         my_file.write("ygvvyuivhui")
#     except Exception as e:
#         print(e)
#     finally:
#         my_file.close()
# except Exception as e:
#     print(e)
#
# # v2
# with open("hello_1.txt", "w") as test_file:
#     test_file.write("wwwwww") # Чаще используется, заменяет собой finally close
#
#
# with open("hello_1.txt", "a") as test_file:
#     test_file.write("rrrrr\ntttttt\n")

#
# with open("hello.txt", "r") as myfile:
#     # v1
#     result = myfile.read()
#     print(result) # Считывается все, что есть в файле
#     # v2
#     result = myfile.readline() # Считывается только первая строка
#     print(result)
#     result = myfile.readline(3) # В данном случае считывается только первых три символа из 1й строки
#     print(result)
#     # v3
#     result = myfile.readlines() # Возвращает список из строк
#     print(result)
#     # v4
#     for line in myfile:
#         print(line, end="") # Пойдет по строкам
#     # v5
#     line = myfile.readline()
#     while line:
#         print(line, end="")
#         line = myfile.readline()

# ###
# FILENAME = "notes.txt"
# NOTES_COUNT = 3
#
# notes = []
#
# for i in range(NOTES_COUNT):
#     notes.append(input(f"Enter note: {i + 1}: ").strip()) # strip Чтобы убрать пробеллы вначале и в конце строки
# #
# with open(FILENAME, "a") as file:
#     for i in range(NOTES_COUNT):
#         file.write(f"{i + 1}. {notes[i]}\n")
# #
# with open(FILENAME, "r") as file:
#     print(file.read())

####
# import pickle # Бинарный режим
# FILENAME = "notes.dat" # dat - дата файл
#
# users = [
#     ["John", "123456789"],
#     ["Peter", "987654321"],
#     ["Vasya", "1568654156"]
# ]
#
# with open(FILENAME, "wb") as file: # wb - write bites
#     pickle.dump(users, file)  # сериализация, т.е. закодирование
#
# with open(FILENAME, "rb") as file:
#     users_from_file = pickle.load(file)  # десериализация
#     for user in users_from_file:
#         print(f"Name: {user[0]} Phone: {user[1]}")

#
# import shelve # Создает вместо 1 файла 3 технических
#
# FILENAME = "notes"
#
# with shelve.open(FILENAME) as users:
#     users["John"] = "123456789"
#     users["Peter"] = "987654321"
#     users["Vasya"] = "1568654156"
#
# with shelve.open(FILENAME) as users:
#     users["Petya"] = "12312341234123"
#     print(users["Petya"])
#     print(users["John"])
#
#     for key in users:
#         print(f"{key} - {users[key]}")
#
#     print(users)
#     users.pop("John", "not found")
#
#     print("-" * 10)
#
#     for key in users:
#         print(f"{key} - {users[key]}")

##########
##
import csv # csv - формат хранения данных наподобие excel, но там просто таблицы, а разделитель иежду ячейками ","

# FILENAME = "users.csv"

# v1
# users = [
#     ["John", "123456789"],
#     ["Peter", "987654321"],
#     ["Vasya", "1568654156"]
# ]
#
# with open(FILENAME, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(users)
# # Флаг newline="" передается в open(), чтобы отключить автоматическое добавление новой строки
# # после каждой записи. Это полезно, чтобы сохранить согласованность форматирования при записи
# # в файл CSV на разных операционных системах.
#
# with open(FILENAME, "a", newline="") as file:
#     user = ["Anton", "87347864786347869"]
#     writer = csv.writer(file)
#     writer.writerow(user)
# # Метод writerows() вызывается на объекте writer и принимает аргумент users.
# # users предполагается, что это итерируемый объект (например, список или кортеж),
# # содержащий данные пользователей, которые вы хотите записать в файл CSV.
#
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(f"{row[0]} - {row[1]}")

# v2 Создание с именем столбцов
# users = [
#     {"name": "John", "phone": "111"},
#     {"name": "Petya", "phone": "222"},
#     {"name": "Vasya", "phone": "333"},
# ]
#
# with open(FILENAME, "w", newline="") as file:
#     columns = ["name", "phone"]
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
    # Этот код также открывает файл с именем, указанным в переменной FILENAME, в режиме записи ("w"),
    # используя конструкцию with open(...) as file. Затем он создает объект файла file.
    #
    # Затем определяется список columns, который содержит имена полей (столбцов) для записи в файл CSV.
    # В данном случае, используются имена "name" и "phone".
    #
    # Далее создается объект writer класса csv.DictWriter, который используется для записи данных
    # в файл CSV в формате словаря. Объект writer связывается с файлом file и принимает два аргумента:
    #
    # fieldnames: это список или кортеж, содержащий имена полей (столбцов) в CSV файле.
    # В данном случае, используется список columns, определенный ранее.
    # file: это объект файла, в который будут записываться данные.
    # Метод writeheader() вызывается на объекте writer для записи заголовка в файл CSV.
    # Заголовок представляет собой строку, содержащую имена полей (столбцов) из списка fieldnames.
    #
    # После записи заголовка, вы можете продолжить записывать данные в файл,
    # используя метод writer.writerow(), который принимает словарь данных для каждой строки
    # в формате {ключ: значение}. Ключи словаря должны соответствовать именам полей (столбцов),
    # определенным в fieldnames.

    # all users
#     writer.writerows(users)
#
#     # one user
#     user: dict = {"name": "Test", "phone": "555"}
#     writer.writerow(user)
#
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['name'], " - ", row['phone'])

###
##
import os

# os.mkdir("test_folder") # Создали папку

# os.rmdir("test_folder") # Удалили папку
#
# file_name = "users.csv"
# if os.path.exists(file_name):
#     os.remove(file_name)
#     print("File removed!")
# else:
#     print("File not found!")

# доп: написать скрипт для удаления всех файлов указанной директории,
# можно написать скрипт для удаления всех файлов, которые начинаются на notes например
#
# # относительный путь - относительно текущей директории (папки где находится исходник который вы запустили)
# with open("f1/f2/test.txt", "w") as myfile:
#     myfile.write("hello world")
# #Чтобы создать папки f1 и f2, нужно правой кнопкой мыши нажать на сам Lesson_11 (над f1)
# и правой кнопкой нажав, выбрать directory. То же самое повторить уже с f1 и в ней создать папку f2

# with open("../../test1.txt", "w") as myfile:
    # myfile.write("hello world")
# Создали файл test1 на 2 уровня выше, относительно файла main, т.е. в папке kirit в моем случае

# абсолютный путь - полный путь начиная с диска C://test_folder/...

# лучше использовать относительные пути, поскольку абсолютные пути не являются универсальными,
# и на каждом устройстве свои