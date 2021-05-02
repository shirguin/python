# Задание №7
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

dict_firms = {}
dict_ave_prof = {}
with open("task_7_lesson5.txt", encoding="utf-8") as f:
    sum_profit = 0
    i = 0
    for line in f:
        ls_line = line.split()
        profit = round((float(ls_line[2]) - float(ls_line[3])), 2)
        dict_firms[ls_line[0]] = profit
        if profit >= 0:# Нулевая прибыль не является убытком
            sum_profit = sum_profit + profit
            i += 1
dict_ave_prof['average_profit'] = round((sum_profit / i), 2)
result_list = [dict_firms, dict_ave_prof]
print(result_list)

'''Сериализация'''
json_result_list = json.dumps(result_list)
print(json_result_list)

with open("task_7_lesson5.json", "w") as write_f:
    json.dump(result_list, write_f)

'''Десериализация'''
with open("task_7_lesson5.json") as read_f:
    load_list = json.load(read_f)
print(load_list)
