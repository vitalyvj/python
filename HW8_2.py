class Error(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Делить на ноль нельзя!'


x = float(input('Введите x: '))
y = float(input('Введите y: '))

try:
    if y == 0:
        raise Error('')
except Error as err:
    print(err)
else:
    print('x / y =', round(x / y, 2))
