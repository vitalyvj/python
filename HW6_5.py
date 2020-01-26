class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(self.title, 'ручкой')


class Pencil(Stationery):
    def draw(self):
        print(self.title, 'карандашом')


class Handle(Stationery):
    def draw(self):
        print(self.title, 'маркером')


stats = [Stationery(''), Pen('Пишем'), Pencil('Чертим'), Handle('Раскрашиваем')]

for stat in stats:
    stat.draw()
