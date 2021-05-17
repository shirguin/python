# Задание №6
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

global in_quantity, in_price


class Warehouse:
    def __init__(self):
        self.nomenclature = {}
        self.nomenclature_b = {}

    # Поступление на склад товара
    def entrance(self, product, quantity, price):
        self.nomenclature[product] = [quantity, price]

    # Убытие товара со склада
    def departure(self, product):
        del self.nomenclature[product]

    # Перемещение товара в другое подразделение
    def moving(self, product):
        self.nomenclature_b[product] = self.nomenclature[product]
        del self.nomenclature[product]

    # Остаток товара на складе "A"
    def balance(self):
        return self.nomenclature

    # Остаток товара в подразделении "B" склада "A"
    def balance_b(self):
        return self.nomenclature_b


class OfficeEquipment:
    def __init__(self, manufacturer, model, color):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, color, printing_technology):
        super().__init__(manufacturer, model, color)
        self.printing_technology = printing_technology
        self.type_equipment = 'принтер'

    def product_card(self):
        card = f'{self.type_equipment} {self.manufacturer} {self.model} {self.color} {self.printing_technology}'
        return card


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, color, permission):
        super().__init__(manufacturer, model, color)
        self.permission = permission
        self.type_equipment = 'сканер'

    def product_card(self):
        card = f'{self.type_equipment} {self.manufacturer} {self.model} {self.color} {self.permission}'
        return card


class CopyMachine(OfficeEquipment):
    def __init__(self, manufacturer, model, color, permission):
        super().__init__(manufacturer, model, color)
        self.permission = permission
        self.type_equipment = 'ксерокс'

    def product_card(self):
        card = f'{self.type_equipment} {self.manufacturer} {self.model} {self.color} {self.permission}'
        return card


# Ввод всех параметров оборудования и оприходывание на склад "A"
def input_product():
    while True:
        while True:
            type_equipment = input('Введите тип оборудования(принтер, сканер, ксерокс): ')
            if type_equipment == 'принтер' or type_equipment == 'сканер' or type_equipment == 'ксерокс':
                break
            else:
                print('Тип оборудования введен неверно!!!')
        manufacturer = input('Введите производителя оборудования: ')
        model = input('Введите модель оборудования: ')
        color = input('Введите цвет оборудования: ')
        if type_equipment == 'принтер':
            printing_technology = input('Введите технологию печати: ')
            product = Printer(manufacturer, model, color, printing_technology).product_card()
            print(product)
            input_quantity()
            input_price()
            wh_a.entrance(product, in_quantity, in_price)
        elif type_equipment == 'сканер':
            permission = 'dpi ' + input('Введите разрешение оборудования: ')
            product = Scanner(manufacturer, model, color, permission).product_card()
            print(product)
            input_quantity()
            input_price()
            wh_a.entrance(product, in_quantity, in_price)
        else:
            permission = 'dpi ' + input('Введите разрешение оборудования: ')
            product = CopyMachine(manufacturer, model, color, permission).product_card()
            print(product)
            input_quantity()
            input_price()
            wh_a.entrance(product, in_quantity, in_price)
        while True:
            temp_exit = input('Хотите ввести следующий товар "да, нет"?: ')
            if temp_exit == 'да' or temp_exit == 'нет':
                break
            else:
                print('Вы ввели не правильную команду!!!')
        if temp_exit == 'нет':
            print('Оприходывание товара завершено!\n')
            break


# Ввод количества оборудования
def input_quantity():
    global in_quantity, in_price
    try:
        in_quantity = int(input('Введите количество этого товара: '))
    except ValueError:
        print('Вы ввели не число!!!')
        input_quantity()
    return in_quantity


# Ввод цены оборудования
def input_price():
    global in_price
    try:
        in_price = float(input('Введите цену этого товара: '))
    except ValueError:
        print('Вы ввели не число!!!')
        input_price()
    return in_price


wh_a = Warehouse()
print('Оприходывание товара  на склад "A"')
input_product()
print(f'Остаток товара на складе "A": {wh_a.balance()}')
print('Программа завершена')
