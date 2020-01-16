# method 1
def my_func_1(x, y):
    return x ** y


# method 2
def my_func_2(x, y):
    z = 1 / x
    for i in range(1, int(abs(y))):
        z = z / x
    return z


x = float(input('Введите x (действительное положительное число): '))
y = float(input('Введите y (целое отрицательное число): '))

if x <= 0 or y >= 0 or y % 1 != 0:
    print('Введенные данные не соответствуют требованиям')
else:
    print(my_func_1(x, y))
    print(my_func_2(x, y))
