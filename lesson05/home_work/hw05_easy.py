# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
for i in range(9):
    a = "dir_" + str(i+1)
    os.mkdir(a)
    
import os
for i in range(9):
    a = "dir_" + str(i+1)
    os.rmdir(a)
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
a = os.getcwd()
print(os.listdir(a))
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
shutil.copyfile(r'11.py', r'11_copy.py')
