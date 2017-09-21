
__author__ = 'Лобанов Дмитрий Викторович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

a = int(input("Введите число и узнаете самую большую цифру в нем:"))
b = a % 10
i = 0
len = len(str(a))
c = 0
while i < len:
    a = a // 10
    c = a % 10
    if  c < b:
        b = b
    else:
        b = c
    i+=1
print(b)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

# первое решение с использованием математики
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
a = a - b
b = b - a
a = b + a
b = a - b + a
print(a)
print(b)

#Второе решение с кортежами
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
a,b = b,a
print(a)
print(b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math
a = 5
b = 5
c = -9
D = b**2 - 4*a*c
if D < 0:
    print("У данного уравнения нет действительных корней")
elif D == 0:
    X = ((b*(-1))+math.sqrt(D))/2*a
    print("Уравнение имеет 1 действительный корень: ", X)
else:
    X = ((b * (-1)) + math.sqrt(D)) / 2 * a
    Y = ((b * (-1)) - math.sqrt(D)) / 2 * a
    print("Уравнение имеет 2 действительных корня:", X, " и ", Y )
