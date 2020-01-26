import time


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self, color):

        if color == 'red' and self.__color == 'green' or self.__color is None:
            self.__color = color
            print('Горит красный')
            time.sleep(7)

        elif color == 'yellow' and self.__color == 'red':
            self.__color = color
            print('Горит желтый')
            time.sleep(2)

        elif color == 'green' and self.__color == 'yellow':
            self.__color = color
            print('Горит зеленый')
            time.sleep(10)

        else:
            print('Нарушен порядок режимов')
            raise SystemExit


tl = TrafficLight()
tl.running('red')
tl.running('yellow')
tl.running('green')
tl.running('red')
tl.running('yellow')
tl.running('green')
tl.running('yellow')
tl.running('green')
