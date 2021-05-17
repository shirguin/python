# Задание №1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def number_from_string(cls, string_date):
        day, month, year = map(int, string_date.split('-'))
        print(string_date)
        return day, month, year

    @staticmethod
    def valid_date(string_date):
        day, month, year = map(int, string_date.split('-'))
        print(string_date)
        if 0 < day <= 31 and 0 < month <= 12 and year <= 2021:
            return day, month, year
        else:
            print('Дата введена не верно!')


d1 = '12-04-1961'
d2 = '17-05-2000'
d3 = '20-13-2021'
print(Date.number_from_string(d1))
print()
print(Date.valid_date(d2))
print()
print(Date.valid_date(d3))
