# Задание №2
# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size, height):
        self.size = size
        self.height = height

    @property
    def fabric_quantity(self):
        return (self.size/6.5+0.5)+(2*self.height+0.3)
    @abstractmethod
    def abstract(self):
        return 'Абстрактный метод'


class Coat(Clothes):

    def fabric_quantity(self):
        return self.size/6.5+0.5

    def abstract(self):
        return 'Абстрактный метод (костюм)'


class Costume(Clothes):

    def fabric_quantity(self):
        return 2*self.height+0.3

    def abstract(self):
        return 'Абстрактный метод (пальто)'


coat = Coat(52, 176)
costume = Costume(52, 176)
print(f'На пошив пальто необходимо {coat.fabric_quantity()} ткани')
print(f'На пошив костюма необходимо {costume.fabric_quantity()} ткани')
print(f'Общее количество ткани для одежды: {coat.fabric_quantity()+costume.fabric_quantity()}')
print(coat.abstract())
print(costume.abstract())
