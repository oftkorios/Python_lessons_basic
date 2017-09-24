# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
a = [2, -5, 8, 9, -25, 25, 4, 2,1,9,2,65,78]
for i in a:
    if i <0:
        a.remove(i)


for r in a:

    if math.sqrt(r)%1 == 0:
        print(int(math.sqrt(r)))

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

# сделал чтобы было интереснее (дата получается текущая)
import datetime
today = datetime.datetime.now()
a = str(today.day)
b = str(today.month)
c = str(today.year)
d = a+'.'+b+'.'+c

day = {
    '01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое',
    '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
    '11': 'одинадцатое', '12': 'двинадцатое', '13': 'тринадцатое', '14': 'четырнадцатое',
    '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое',
    '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе',
    '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое',
    '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое',
    '31': 'тридцать первое',
    #добавление чисел для тех кто введет число без нуля
    '1': 'первое', '2': 'второе', '3': 'третье', '4': 'четвертое', '5': 'пятое',
    '6': 'шестое', '7': 'седьмое', '8': 'восьмое', '9': 'девятое'
}
month = {
    '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
    '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря',
    # добавление чисел для тех кто введет месяц без нуля
    '1': 'января', '2': 'февраля', '3': 'марта', '4': 'апреля', '5': 'мая', '6': 'июня',
    '7': 'июля', '8': 'августа', '9': 'сентября'
}
print(day[a],month[b], c,"года")

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
a = []
n = int(input("Введите количество элементов в списке:"))
for i in range(n):
    b = random.randint(-100,100)
    a.append(b)
print(a)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
