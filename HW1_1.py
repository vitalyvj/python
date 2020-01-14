number = 10
print(number)
print(type(number))

pi = 3.14
print(pi)
print(type(pi))

name = 'Ivan'
print(name)
print(type(name))

is_man = True
print(is_man)
print(type(is_man))

var_list = [number, pi, name, is_man]
print(var_list)
print(type(var_list))

var_tuple = (number, pi, name, is_man)
print(var_tuple)
print(type(var_tuple))

var_set = {number, pi, name, is_man}
print(var_set)
print(type(var_set))

name = input('Введите Ваше имя: ')
surname = input('Введите Вашу фамилию: ')
gazp_buy = int(input('По какой цене Вы купили акции Газпрома?: '))
gazp_sum = int(input('На какую сумму Вы купили акции Газпрома?: '))
gazp_now = 255
if gazp_buy < gazp_now:
    print(f'Позравляем Вас, {name} {surname}! Вы заработали {(gazp_now / gazp_buy - 1) * gazp_sum:.2f} рублей!')
else:
    print('К сожалению, инвестиции в национальное достояние для Вас не оказались прибыльными. Подождите роста курса '
          'акций, нам сказали, что он обязательно будет))')
    
