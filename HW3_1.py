def my_func(x, y):
    return x / y


x = float(input('Введите числитель: '))
y = float(input('Введите знаменатель: '))

try:
    print(my_func(x, y))
except ZeroDivisionError:
    print('Разделить на ноль, к сожалению, не получится')
