number = int(input('Введите время в секундах: '))
hour = number // 3600
minute = number // 60 - hour * 60
second = number - minute * 60 - hour * 3600

print(f'Точное время {str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}')
