# Задание №6 часть 2
# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
# завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
# повторение элементов списка прекратится.

from sys import argv
from itertools import cycle
task_6_1_lesson4, number_rep = argv
''' Определение параметров

task_6_lesson4 - имя скрипта
number_rep - число повторений элементов списка

'''
a = 1
my_list = ['Hello', 'World']
for el in cycle(my_list):
    if a > int(number_rep):
        break
    else:
        print(el)
        a += 1
