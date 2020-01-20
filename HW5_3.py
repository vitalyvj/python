staff_20 = []
salary_sum = 0
i = 0

with open('file5_3.txt', encoding='utf-8') as f:

    for el in f.readlines():
        surname = el.split()[0]
        salary = int(el.split()[1])
        salary_sum += salary
        if salary < 20000:
            staff_20.append(surname)
        i += 1

print(f'Средняя зарплата {salary_sum / i:.2f} руб.')
print(f'Сотрудники, получающие зарплату менее 20 тыс. руб.:')
for el in staff_20:
    print(el)

