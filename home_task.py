# 1. Дан текстовый файл. Необходимо создать новый файл, в который требуется
# переписать из исходного файла все слова, состоящие не менее чем из семи букв.
#
# import re
# # try:
# #     with open("files_forTask/first_task.txt", "w") as my_file:
# #         my_file.write("I can resist everything except temptation.\nI have the simplest tastes. I am always satisfied with the best.\n")
# # except Exception as error:
# #     print(error)
#
# try:
#     with open("files_forTask/first_task.txt", "r") as file_to_read:
#         result = file_to_read.read()
#         print(result)
#         words_seven = re.findall(r'\b\w{7,}\b', result)
#         print(words_seven)
#
# except Exception as error:
#     print(error)
#
# try:
#     # with open("files_forTask/first_task_words.txt", "a") as file_to_append:
#     #     for i in range(len(words_seven)):
#     #         file_to_append.write(f"{i+1}: {words_seven[i]}\n")
#
#     with open("files_forTask/first_task_words.txt", "r") as file:
#         result = file.read()
#         print(result)
# except Exception as error:
#     print(error)
#
# 2. Дан текстовый файл. Подсчитать количество слов в нём.

# V1
# try:
#     with open("files_forTask/sec_task.txt", "w") as myfile:
#         myfile.write("Experience is simply the name we give our mistakes.\nArt never express anything but itself.\n")
# except Exception as error:
#     print(error)

# try:
#     with open("files_forTask/sec_task.txt", "r") as file_to_read:
#        result = file_to_read.readlines()
#        print(result)
#
#        word = 0
#        SEPARATOR = " "
#        for line in result:
#            words = line.split(SEPARATOR)
#            print(words)
#            word += len(words)
#
#     print(f"There are {word} separate words!")
#
# except Exception as error:
#     print(error)

# V2

# import re
#
# try:
#     with open("files_forTask/sec_task.txt", "r") as my_file:
#         result = my_file.read()
#         list_of_words = re.findall(r'\b\w+\b', result) # Ищем любые совпадения с паттерном 1 или более цифра/буква в границах слова
#         print(list_of_words)
#         word = len(list_of_words)
#         print(f"There are {word} separate words!")
# except Exception as error:
#     print(error)
