class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.color, self.name, 'started')

    def stop(self):
        print(self.color, self.name, 'stopped')

    def turn(self, direction):
        print(self.color, self.name, 'turned', direction)

    def show_speed(self):
        print('Current speed', self.speed, 'km/h')

    def police_car(self):
        if self.is_police:
            print("Clear the road! It's a police car!")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print('Current speed', self.speed, 'km/h')
        if self.speed > 60:
            print('Over speed! Slow down!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print('Current speed', self.speed, 'km/h')
        if self.speed > 40:
            print('Over speed! Slow down!')


class PoliceCar(Car):
    def __init__(self, speed, color='Blue', name='Lada', is_police=True):
        super().__init__(speed, color, name, is_police)


cars = [TownCar(80, 'White', 'Toyota'), SportCar(250, 'Yellow', 'Lamborghini'), WorkCar(45, 'Black', 'KAMAZ'),
        PoliceCar(100)]

for car in cars:
    car.go()
    car.turn('left')
    car.show_speed()
    car.police_car()
    car.turn('right')
    car.stop()
    print()
