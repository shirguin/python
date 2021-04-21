# Задание №3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    if arg_1 > arg_3 and arg_2 > arg_3:
        return arg_1 + arg_2
    elif arg_1 > arg_2 and arg_3 > arg_2:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3


arg_1 = float(input('Введите первый аргумент:'))
arg_2 = float(input('Введите второй аргумент:'))
arg_3 = float(input('Введите третий аргумент:'))
print(my_func(arg_1, arg_2, arg_3))
