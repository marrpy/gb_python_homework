# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'Машина {self.name} остановилась.'

    def turn(self, direction):
        return f'Машина {self.name} повернула {direction}.'

    def show_speed(self):
        return f'Скорость составила: {self.speed}.'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Вы превысили скорость! Ваша скорость составляет {self.speed}.'
        else:
            return f'Ваша скорость составляет {self.speed}.'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили скорость! Ваша скорость составляет {self.speed}.'
        else:
            return f'Ваша скорость составляет {self.speed}.'

class PoliceCar(Car):
    pass

town = TownCar(70, 'grey', 'Lada Granta', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar(150, 'black', 'Audi R8', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar(100, 'white', 'Nissan', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar(80, 'blue', 'Kia', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('right'), police.stop())