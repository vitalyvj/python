class Error(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Введенные данные не являются числом! Попробуйте еще раз'


number = ''
numbers_list = []

while number != 'stop':
    number = input('Введите число (для окончания введите stop): ')
    try:
        if number.isdigit():
            numbers_list.append(number)
        elif number == 'stop':
            print('Итоговый список введенных чисел:', numbers_list)
        else:
            raise Error('')
    except Error as err:
        print(err)
