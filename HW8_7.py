class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{} + {}i'.format(self.x, self.y)

    def __add__(self, other):
        return '{} + {}i'.format(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return '{} + {}i'.format(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)


a = Complex(8, 5)
b = Complex(6, 3)

print('a =', a)
print('b =', b)
print('a + b =', a + b)
print('a * b =', a * b)