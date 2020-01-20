numbers = input('Введите числа: ')

with open('file5_5.txt', 'w+') as f:
    f.write(numbers)
    f.seek(0)
    numbers_file = f.read().split()
    numbers_float = map(float, numbers_file)
    print(sum(numbers_float))
