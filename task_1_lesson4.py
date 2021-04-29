# Задание №1
# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.

from sys import argv
task_1_lesson4, number_hours, rate_hour, bonus = argv
''' Определение параметров

task_1_lesson4 - имя скрипта
number_hours - Количество отработанных часов
rate_hour - Ставка в час
bonus - Сумма премии

'''
print(f'Количество отработанных часов: {number_hours}')
print(f'Ставка в час: {rate_hour}')
print(f'Сумма премии: {bonus}')
salary = round((float(number_hours) * float(rate_hour) + float(bonus)), 2)
print(f'Заработная плата сотрудника: {salary} руб.')
