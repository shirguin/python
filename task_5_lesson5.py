# Задание №5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

'''Создается текстовый файл со строками чисел'''
with open("task_5_lesson5.txt", "at", encoding="utf-8") as f:
    while True:
        str_numbers = input('Введите строку чисел, разделенных пробелами: ')
        f.write(f'{str_numbers}\n')
        exit_question = input('Введите "exit", если больше не нужно вводить строку чисел: ')
        if exit_question == 'exit':
            break

'''Подсчет суммы чисел в файле'''
with open("task_5_lesson5.txt", encoding="utf-8") as f:
    i = 1
    sum_file = 0
    for line in f:
        ls_number_line = line.split()
        sum_line = 0
        for el in ls_number_line:
            sum_line = sum_line + float(el)
        print(f'Сумма чисел в строке {i} равна {round(sum_line, 2)}')
        sum_file = sum_file + sum_line
        i += 1
print(f'Сумма всех чисел в файле task_5_lesson5.txt равна: {round(sum_file, 2)}')
