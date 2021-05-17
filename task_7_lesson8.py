# Задание №7
# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a + other.a}+{self.b + other.b}*i'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b}+{self.a * other.b + other.a * self.b}*i'

    def __str__(self):
        return f'{self.a}+{self.b}*i'


comp_1 = ComplexNumber(1, 2)
comp_2 = ComplexNumber(3, 4)
print(f'Комплексное число №1: ({comp_1})')
print(f'Комплексное число №2: ({comp_2})')
print(f'Сумма комплексных чисел равна: ({comp_1 + comp_2})')
print(f'Произведение комплексных чисел равно: ({comp_1 * comp_2})')
print('Программа завершена')
