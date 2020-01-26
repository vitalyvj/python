class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print('Имя сотрудника:', self.name, self.surname)

    def get_total_income(self):
        print('Доход сотрудника:', sum(self._income.values()))


worker_1 = Position('Иван', 'Иванов', 'директор', 200000, 500000)
worker_1.get_full_name()
worker_1.get_total_income()

worker_2 = Position('Петр', 'Петров', 'главбух', 150000, 200000)
worker_2.get_full_name()
worker_2.get_total_income()
