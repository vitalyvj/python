class Warehouse:

    @staticmethod
    def presence():
        for el in Warehouse.warehouse_list:
            print(el)

    @staticmethod
    def move_to_office(title, quantity, department):
        for el in Warehouse.warehouse_list:
            for key, val in el.items():
                if title == val:
                    if quantity <= el['количество']:
                        el['количество'] -= quantity
                        if el['количество'] == 0:
                            Warehouse.warehouse_list.remove(el)
                        return print(
                            f'{title} в количестве {quantity} шт. перемещен в подразделение: {department}')
                    else:
                        return print('Весь товар в офисе')

    warehouse_list = []


class Error(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Цена и количество товаров должны быть числовыми параметрами!'


class Equipment:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

        try:
            if type(self.price) != int or type(self.quantity) != int:
                raise Error('')
        except Error as err:
            print(err)
            raise SystemExit

    @staticmethod
    def presence():
        if not Equipment.equipment_list:
            print('Оргтехника на складе')
        else:
            for el in Equipment.equipment_list:
                print(el)

    @staticmethod
    def move_to_warehouse():
        Warehouse.warehouse_list.extend(Equipment.equipment_list)
        Equipment.equipment_list = []
        print('Техника передана на склад')

    equipment_list = []


class Printer(Equipment):
    def __init__(self, title, price, quantity, color):
        super().__init__(title, price, quantity)
        self.color = color
        Equipment.equipment_list.append({'наименованиe': self.title, 'цена': self.price, 'количество': self.quantity,
                                         'цветной или ч/б': self.color})


class Scanner(Equipment):

    def __init__(self, title, price, quantity, resolution):
        super().__init__(title, price, quantity)
        self.resolution = resolution
        Equipment.equipment_list.append({'наименованиe': self.title, 'цена': self.price, 'количество': self.quantity,
                                         'разрешение': self.resolution})


class Xerox(Equipment):
    def __init__(self, title, price, quantity, capacity):
        super().__init__(title, price, quantity)
        self.capacity = capacity
        Equipment.equipment_list.append(
            {'наименованиe': self.title, 'цена': self.price, 'количество': self.quantity, 'разрешение': self.capacity})


Printer('HP Laser Jet', 20000, 3, 'цветной')
Scanner('Canon', 10000, 2, '600 dpi')
Xerox('Xerox', 30000, 5, '500 листов в мин')

Equipment.presence()
Equipment.move_to_warehouse()
Equipment.presence()
Warehouse.move_to_office('HP Laser Jet', 3, 'отдел продаж')
Warehouse.move_to_office('Xerox', 2, 'отдел закупок')

Printer('HP Laser Jet', 'asd', 'qwe', 'цветной')
