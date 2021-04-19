# Задание №5
# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
# не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
number = int(input('Введите число: '))
print(f'Рейтинг до ввода:    {my_list}')
number_rep = my_list.count(number)
if number_rep > 0:
    i = my_list.index(number)
    my_list.insert(i+number_rep, number)
else:
    if number > my_list[0]:
        my_list.insert(0, number)
    else:
        my_list.append(number)
print(f'Рейтинг после ввода: {my_list}')
