# Задание №2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionZero(Exception):
    def __init__(self, text):
        self.text = text


try:
    divisible = float(input('Введите делимое число: '))
    divisor = float(input('Введите делитель: '))
    if divisor == 0:
        raise DivisionZero('Вы ввели ноль, деление на ноль невозможно!')
except ValueError:
    print('Вы ввели не число')
except DivisionZero as err:
    print(err)
else:
    print(f'Результат деления равен: {round((divisible / divisor), 2)}')
print('Программа завершена')
