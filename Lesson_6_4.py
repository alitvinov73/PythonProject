# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.

class Car:
    is_police = False

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def go(self, speed):
        self.speed = speed
        print(f'Car {self.name} is going, speed is {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'Car {self.name} is stop')

    def turn_direction(self, direction):
        print(f'Car {self.name} is turn to {"left" if direction == "left" else "right"}')

    def show_speed(self):
        print(f'Speed {self.name} is {self.speed}')


class TownCar(Car):
    # 60(TownCar)
    def show_speed(self):
        print(f'{self.name} speed is {self.speed} and exceeded by {self.speed-60}' \
            if int(self.speed) > 60 else f'{self.name} speed is {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    # 40(WorkCar)
    def show_speed(self):
        print(f'{self.name} speed is {self.speed} and exceeded by {self.speed - 40}' \
                  if int(self.speed) > 40 else f'{self.name} speed is {self.speed}')


class PoliceCar(Car):
    is_polise = True


town_car = TownCar("Lexus", "black", 70)
town_car.go(20)
town_car.turn_direction("left")
town_car.turn_direction("right")
town_car.go(70)
town_car.show_speed()
town_car.stop()

work_car = WorkCar("Kamaz", "grey", 20)
work_car.go(20)
work_car.turn_direction("left")
work_car.turn_direction("right")
work_car.go(60)
work_car.show_speed()
work_car.stop()

sport_car=SportCar("Mazda", "white", 200)
sport_car.go(20)
sport_car.turn_direction("left")
sport_car.turn_direction("right")
sport_car.go(250)
sport_car.show_speed()
sport_car.stop()

police_car=PoliceCar("Bobik", "green", 50)
police_car.go(20)
police_car.turn_direction("left")
police_car.turn_direction("right")
police_car.go(80)
police_car.show_speed()
police_car.stop()
