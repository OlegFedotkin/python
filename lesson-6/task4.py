# 4) Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print(f'{self.color} {self.name} поехала')

    def stop(self):
        if self.speed == 0:
            print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        if self.speed == 0:
            if direction == 1:
                print(f'{self.color} {self.name} повернула налево')
            elif direction == 2:
                print(f'{self.color} {self.name} повернула направо')
        else:
            if direction == 1:
                print(f'{self.color} {self.name} повернула налево')
            elif direction == 2:
                print(f'{self.color} {self.name} повернула направо')

    def show_speed(self):
        if self.speed > 0:
            print(f'Скорость {self.name} {self.speed} км/ч')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, body_car):
        super().__init__(speed, color, name, is_police)
        self.body_car = body_car

    def body_of_the_car(self):
        print(f'Кузов {self.name} {self.body_car}')

    def show_speed(self):
        if self.speed > 0:
            print(f'Скорость {self.name} {self.speed} км/ч')
        if self.speed > 60:
            print(f'{self.name} превысила скорость!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police, body_car):
        super().__init__(speed, color, name, is_police)
        self.body_car = body_car

    def body_of_the_car(self):
        print(f'Кузов {self.name} {self.body_car}')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, body_car):
        super().__init__(speed, color, name, is_police)
        self.body_car = body_car

    def body_of_the_car(self):
        print(f'Кузов {self.name} {self.body_car}')

    def show_speed(self):
        if self.speed > 0:
            print(f'Скорость {self.name} {self.speed} км/ч')
        if self.speed > 40:
            print(f'{self.name} превысила скорость!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, body_car):
        super().__init__(speed, color, name, is_police)
        self.body_car = body_car
    def body_of_the_car(self):
        print(f'Кузов {self.name} {self.body_car}')

c1 = TownCar(90, 'белая', 'Toyota', False, 'универсал')
c1.go()
c1.stop()
c1.turn(2)
c1.show_speed()
c1.body_of_the_car()
print('_' * 50)
c2 = SportCar(0, 'красная', 'Лада', False, 'седан')
c2.go()
c2.stop()
c2.turn(1)
c2.show_speed()
c2.body_of_the_car()
print('_' * 50)
c3 = WorkCar(50, 'красная', 'DAF', False, 'track')
c3.go()
c3.stop()
c3.turn(0)
c3.show_speed()
c3.body_of_the_car()
print('_' * 50)
c4 = PoliceCar(120, 'красная', 'Daewoo', True, 'седан')
c4.go()
c4.stop()
c4.turn(2)
c4.show_speed()
c4.body_of_the_car()
