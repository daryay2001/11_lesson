import os

try:
    directory = os.getcwd()
    print(directory)
except Exception as error:
    print(error)