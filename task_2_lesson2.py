# Задание №2
# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
# input().

number_elements = int(input('Введите количество элементов списка: '))
input_list = []
i = 0
while i <= (number_elements - 1):
    el = input(f'Введите {i} элемент списка: ')
    input_list.append(el)
    i += 1
print('Список пользователя: ', input_list)

i = 0
while i <= (number_elements // 2):
    el = input_list[i + 1]
    input_list.pop(i+1)
    input_list.insert(i, el)
    i += 2
print('Измененный список  : ', input_list)
