def my_func(a, b, c):
    d = min(a, b, c)
    return a + b + c - d


a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

print(my_func(a, b, c))
