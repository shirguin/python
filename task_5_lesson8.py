# Задание №5
# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру (например, словарь).

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

    # Перемещение товара в подразделение "B"
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


# Создаем оргтехнику
pr_1 = Printer('Epson', 'TX659', 'серый', 'струйный')
print(pr_1.product_card())
sc_1 = Scanner('Epson', 'EX897', 'черный', 'dpi 600x1200')
print(sc_1.product_card())
cm_1 = CopyMachine('Xerox', 'X7856S', 'белый', 'dpi 1200x1200')
print(cm_1.product_card())

# Создаем склад и перемещаем на него оргтехнику
wh_a = Warehouse()
wh_a.entrance(pr_1.product_card(), 15, 8500)
wh_a.entrance(sc_1.product_card(), 5, 4200)
wh_a.entrance(cm_1.product_card(), 10, 15000)

# Смотрим остаток товара
print(f'Остаток товара на складе "A": {wh_a.balance()}')

# Расход товара со склада "A"
wh_a.departure(sc_1.product_card())
print(f'Остаток товара на складе "A": {wh_a.balance()}')

# Перемещение товара со склада "A" в подразделение "B"
wh_a.moving(cm_1.product_card())
print(f'Остаток товара на складе "A": {wh_a.balance()}')
print(f'Остаток товара в подразделении "B" склада "A": {wh_a.balance_b()}')
print('Программа завершена')
