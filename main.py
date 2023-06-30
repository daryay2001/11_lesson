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
#     test_file.write("wwwwww")
#
#
# with open("hello_1.txt", "a") as test_file:
#     test_file.write("rrrrr\ntttttt\n")

#
# with open("hello.txt", "r") as myfile:
#     # v1
#     # result = myfile.read()
#     # print(result)
#     # v2
#     # result = myfile.readline()
#     # print(result)
#     # result = myfile.readline(3)
#     # print(result)
#     # v3
#     # result = myfile.readlines()
#     # print(result)
#     # v4
#     # for line in myfile:
#     #     print(line, end="")
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
#     notes.append(input(f"Enter note: {i + 1}: ").strip())
#
# with open(FILENAME, "a") as file:
#     for i in range(NOTES_COUNT):
#         file.write(f"{i + 1}. {notes[i]}\n")
#
# with open(FILENAME, "r") as file:
#     print(file.read())

####
# import pickle
# FILENAME = "notes.dat"
#
# users = [
#     ["John", "123456789"],
#     ["Peter", "987654321"],
#     ["Vasya", "1568654156"]
# ]
#
# with open(FILENAME, "wb") as file:
#     pickle.dump(users, file)  # сериализация
#
# with open(FILENAME, "rb") as file:
#     users_from_file = pickle.load(file)  # десериализация
#     for user in users_from_file:
#         print(f"Name: {user[0]} Phone: {user[1]}")

#
# import shelve
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
import csv

FILENAME = "users.csv"

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
#
# with open(FILENAME, "a", newline="") as file:
#     user = ["Anton", "87347864786347869"]
#     writer = csv.writer(file)
#     writer.writerow(user)
#
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(f"{row[0]} - {row[1]}")

# v2
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
#
#     # all users
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
# import os

# os.mkdir("test_folder")

# os.rmdir("test_folder")
#
# file_name = "users.csv"
# if os.path.exists(file_name):
#     os.remove(file_name)
#     print("File removed!")
# else:
#     print("File not found!")

# доп: написать скрипт для удаления всех файлов указанной директории
#
# # относительный путь - относительно текущей директории (папки где находится исходник который вы запустили)
# with open("f1/f2/test.txt", "w") as myfile:
#     myfile.write("hello world")
# #
# with open("../../test1.txt", "w") as myfile:
#     myfile.write("hello world")
# абсолютный путь - полный путь начиная с диска C://test_folder/...

