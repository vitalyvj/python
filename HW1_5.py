revenue = int(input('Введите выручку в рублях: '))
costs = int(input('Введите себестоимость в рублях: '))
profit = revenue - costs

if profit >= 0:
    print(f'Прибыль составила {profit} рублей')
    print(f'Рентабельность выручки {profit / revenue * 100:.1f}%')
    num_employees = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль фирмы на одного сотрудника составила {profit / num_employees} рублей')

else:
    print(f'Убыток составил {costs - revenue} рублей. Похоже, что надо сокращать численность сотрудников.')
