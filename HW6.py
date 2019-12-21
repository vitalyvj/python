a = int(input('Введите a: '))
b = int(input('Введите b: '))
i = 1

while a <= b:
    a = a * 1.1
    i += 1

print(i)

print(f'На {i} день спортсмен достиг результата - не менее {int(a)} км')
