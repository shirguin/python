# задание№1
# Поработайте с переменными, создайте несколько, выведите на
# экран. Запросите у пользователя некоторые числа и строки и
# сохраните в переменные, затем выведите на экран.

name = input('Введите Ваше имя: ')
surname = input('Введите Вашу фамилию: ')
age = int(input('Введите Ваш возраст: '))
year_birth = 2021 - age
print(f'Добрый день {name} {surname}, Вы родились в {year_birth} году и Вам {age} лет')
