# Задание №6 часть 1
# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
# завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
# повторение элементов списка прекратится.

from sys import argv
from itertools import count
task_6_lesson4, start_number = argv
''' Определение параметров

task_6_lesson4 - имя скрипта
start_number - число с которого начинать формировать список

'''
for el in count(int(start_number)):
    if el > 10:
        break
    else:
        print(el)
