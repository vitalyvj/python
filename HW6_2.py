class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        print('Сформирован объект дороги длиной {} м и шириной {} м'.format(length, width))

    def calc(self, weight, thick):
        return self._length * self._width * weight * thick


my_length = int(input('Введите длину дороги в метрах: '))
my_width = int(input('Введите ширину дороги в метрах: '))

road = Road(my_length, my_width)

my_weight = int(input('Введите удельный расход асфальта в кг/м2*см: '))
my_thick = int(input('Введите толщину полотна в см: '))

print('Для строительства дороги необходимо', road.calc(my_weight, my_thick) / 1000, 'тонн асфальта')
