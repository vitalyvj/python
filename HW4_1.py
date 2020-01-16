def salary():
    return float(production) * float(rate) + float(bonus)


from sys import argv

filename, production, rate, bonus = argv

print('Выработка в часах: ', production, 'часов')
print('Ставка в час: ', rate, 'рублей в час')
print('Премия: ', bonus, 'рублей')
print('Заработная плата сотрудника: ', salary(), 'рублей')
