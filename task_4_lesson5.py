# Задание №4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

dict_number = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
new_ls = []
out_file = open("task_4_lesson5_2.txt", "at", encoding="utf-8")
with open("task_4_lesson5_1.txt", encoding="utf-8") as in_file:
    for line in in_file:
        temp = line.split()
        len_key = len(temp[0])
        key = temp[0]
        out_file.write(dict_number[key]+line[len_key:])
out_file.close()
