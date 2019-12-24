month = int(input('Введите номер месяца в виде числа: '))

while month < 1 or month > 12:
    print('Вы изобрели новый календарь! Но пока давайте будем пользоваться старым')
    month = int(input('Введите номер месяца в виде числа: '))

# через dict
seasons_dict = {'зима': (12, 1, 2), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
for seasons, months in seasons_dict.items():
    if month in months:
        print(seasons)

# через list
seasons_list = ['зима', 'весна', 'лето', 'осень']
if 3 <= month <= 5:
    season = seasons_list.pop(1)
elif 6 <= month <= 8:
    season = seasons_list.pop(2)
elif 9 <= month <= 11:
    season = seasons_list.pop(3)
else:
    season = seasons_list.pop(0)
print(season)
