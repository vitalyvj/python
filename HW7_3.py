class Cell:
    def __init__(self, parts):
        self.parts = int(parts)

    def __add__(self, other):
        return self.parts + other.parts

    def __sub__(self, other):
        if self.parts - other.parts > 0:
            return self.parts - other.parts
        else:
            return 'Разность ячеек двух клеток меньше нуля'

    def __mul__(self, other):
        return self.parts * other.parts

    def __truediv__(self, other):
        return self.parts // other.parts

    def make_order(self, n):
        string = str()
        for i in range(self.parts // n):
            string += '*' * n + '\n'
        string += '*' * (self.parts % n)
        print('\nКлетка с {} ячейками'.format(self.parts))
        print(string)


cell_1 = Cell(28)
cell_2 = Cell(11)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

cell_1.make_order(5)
cell_2.make_order(3)
