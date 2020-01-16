numbers_sum = 0
el = None

while el != 'Q':

    numbers = input('Для выхода введите Q \n'
                    'Введите числа через пробел: ')
    numbers_str = numbers.split()

    for el in numbers_str:
        if el == 'Q':
            numbers_str.remove(el)

    try:
        numbers_float = list(map(float, numbers_str))
    except ValueError:
        print('Вы можете вводить только числа либо Q')
        continue

    numbers_sum = sum(numbers_float) + numbers_sum
    print(f'Общая сумма чисел: {numbers_sum}')
