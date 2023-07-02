# доп: написать скрипт для удаления всех файлов указанной директории,
# можно написать скрипт для удаления всех файлов, которые начинаются на notes например.
import os

# file_name = "hello_1.txt"
# if os.path.exists(file_name):
#     os.remove(file_name)
#     print("File removed!")
# else:
#     print("File not found!")

# try:
#     with open("files_to_add_delete/notes1.txt", "w") as file:
#         file.write("We are all in the gutter, but some of us are looking at the stars.")
#
#     with open("files_to_add_delete/notes2.txt", "w") as myfile:
#         myfile.write("Life imitates art far more than art imitates Life.")
#
#     with open("files_to_add_delete/notes3.txt", "w") as another_file:
#         another_file.write("The play was a great success, but the audience was a failure.")
#
#     with open("files_to_add_delete/some_text.txt", "w") as any_file:
#         any_file.write("You can never be overdressed or overeducated.")
#
# except Exception as error:
#     print(error)
try:
    # direct = input((f"Enter path: ").strip())
    direct = "/files_to_add_delete/"
    if os.path.exists(direct):
        print("Path exist")
    #     for file_name in os.listdir(direct): #Проверка наличия файлов в директории
    #         # if file_name.startswith(input((f"Enter file name to delete: ").strip()):
    #         if file_name.startswith("notes"):
    #             file_path = os.path.join(direct, file_name)
    #             os.remove(file_path)
    #             print(f"File {file_name} was deleted")
    else:
        print("Such path is not exist!")

except Exception as error:
    print(error)
