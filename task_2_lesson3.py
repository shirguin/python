# Задание №2
# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.

def data_entry():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    year_birth = input('Введите год рождения: ')
    city_residence = input('Введите город проживания: ')
    email = input('Введите email: ')
    telephone = input('Введите телефон: ')
    data = ' '.join([name, surname, year_birth, city_residence, email, telephone])
    return data


print(data_entry())
