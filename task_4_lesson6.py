# Задание №4
# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула на право'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def show_speed(self):
        return f'Текущая скорость {self.name} состовляет {self.speed} км/час'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} состовляет {self.speed} км/ч')
        if self.speed == 0:
            return f'{self.name} стоит недвижимо'
        elif self.speed > 60:
            return f'{self.name} превышает скорость'
        else:
            return f'Скорость {self.name} в пределах нормы'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} состовляет {self.speed}')
        if self.speed == 0:
            return f'{self.name} стоит недвижимо'
        elif self.speed > 40:
            return f'{self.name} превышает скорость'
        else:
            return f'Скорость {self.name} в пределах нормы'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name}, является полицейской машиной'
        else:
            return f'{self.name}, не является полицейской машиной'


kia = TownCar(80, 'белый', 'kia', False)
print(kia.go())
print(kia.stop())
print(kia.turn_left())
print(kia.turn_right())
print(kia.show_speed())

porsche = SportCar(150, 'красный', 'Porsche', False)
print(porsche.go())
print(porsche.show_speed())

lada = WorkCar(50, 'зеденый', 'Lada', False)
print(lada.go())
print(lada.show_speed())

patriot = PoliceCar(60, 'черный', 'Patriot', True)
print(patriot.turn_left())
print(patriot.turn_right())
print(patriot.police())
