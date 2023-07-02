# Создайте приложение, проверяющее текст на недопустимые слова.
#
# Если недопустимое слово найдено, оно должно быть заменено на набор символов *.
#
# По итогам работы приложения необходимо показать статистику действий.

#
# try:
#     with open("files_for_addTasks/file_to_replace.txt", "w") as file:
#         file.write("I met a little Elf-man, once,\n"
#                    "Down where the lillies blow.\n"
#                    "I asked him why he was so small,\n"
#                    "And why he didn't grow.\n"
#                    "He slightly frowned, and with his eye\n"
#                    "He looked me through and through.\n"
#                    "I'm just  as big for me, said he\n"
#                    "As you are big for you.\n")
# except Exception as error:
#     print(error)

# def replace_word(text, word_to_replace):
#     stars = "*" * len(word_to_replace)
#     text = text.replace(word_to_replace, stars)
#     return text
#
# try:
#     with open("files_for_addTasks/file_to_replace.txt", "r") as file:
#         result = file.read()
#
#         word = input((f"Enter your word to replace: ").strip())
#         if word in result:
#             result_2 = replace_word(result, word)
#             print(result_2)
#             counter = result.count(word)
#             print(f"{counter} words were replaced!")
#             with open("files_for_addTasks/file_with_stars.txt", "w") as myfile:
#                 text = myfile.write(result_2)
#         else:
#             print("There is no such word!")
#
# except Exception as error:
#     print(error)





