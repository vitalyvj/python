number = input('Введите целое положительное число: ')

length = len(number)
i = 0
max_number = 0

while i < length:
    current_number = int(number[i])
    if max_number < current_number:
        max_number = current_number
    i += 1

print(max_number)

