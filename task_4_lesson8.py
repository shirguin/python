# Задание №4
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self):
        self.nomenclature = []

    # Поступление на склад товара
    def entrance(self, product):
        self.nomenclature.append(product)

    # Убытие товара со склада
    def departure(self, product):
        self.nomenclature.remove(product)

    # Остаток товара на складе
    def balance(self):
        return self.nomenclature


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


# Создаем оргтехнику
pr_1 = Printer('Epson', 'TX659', 'серый', 'струйный')
print(pr_1.product_card())
sc_1 = Scanner('Epson', 'EX897', 'черный', 'dpi 600x1200')
print(sc_1.product_card())
cm_1 = CopyMachine('Xerox', 'X7856S', 'белый', 'dpi 1200x1200')
print(cm_1.product_card())

# Создаем склад и перемещаем на него оргтехнику
wh = Warehouse()
wh.entrance(pr_1.product_card())
wh.entrance(sc_1.product_card())
wh.entrance(cm_1.product_card())

# Смотрим остаток товара
print(f'Остаток товара на складе {wh.balance()}')

# Перемещаем товар со склада
wh.departure(sc_1.product_card())
print(f'Остаток товара на складе {wh.balance()}')
