import os
import shutil
def welcome_function():
    print("\n"+" 1. Перейти в папку")
    print(" 2. Просмотреть содержимое текущей папки")
    print(" 3. Удалить папку")
    print(" 4. Создать папку")
    print(" 5. Завершить работу","\n")


def go_over_to_path():
    path = str(input("Введи директорию: "))
    if os.path.exists(path) == True:
        os.chdir(path)
        print("Успешно перешел в директорию",path)
    else:
        print("Невозможно перейти! Директории", path,"не существует!")
    print("Текущая директория", os.getcwd())
    welcome_function()

def get_list_path():
    path = os.getcwd()
    print("Текущая директория", path)
    print("Содержимое директории:",os.listdir(path))
    welcome_function()

def del_path():
    path = str(input("Введи название директории для удаления:"))
    if os.path.exists(path)== True:
        shutil.rmtree(path)
        print("Директория",path, " успешно удалена!")
    else:
        print("Невозможно удалить директорию", str(path)+".","Такой директории не существует!")
    print("Текущая директория", os.getcwd())
    welcome_function()

def create_path():
    path = str(input("Введи название директории для создания:"))
    if os.path.exists(path) == True:
        print("Директория", path, "уже существует!")
    else:
        os.mkdir(path)
        print("Директория", path, "успешно создана!")
    print("Текущая директория", os.getcwd())
    welcome_function()
