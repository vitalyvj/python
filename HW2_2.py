len_list = int(input('Введите количество элементов в списке: '))
my_list = []
i = 1
j = 0

while i <= len_list:
    my_list.append(input(f'Введите {i} элемент списка: '))
    i += 1
print(my_list)

while j < len_list:
    item = my_list.pop(j)
    my_list.insert(j + 1, item)
    j += 2
print(my_list)
