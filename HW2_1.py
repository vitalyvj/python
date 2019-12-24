my_list = ['Hello', 100, 3.14, True, None, [1, 2, 3], (1, 2, 3), {1, 2, 3}]
i = len(my_list)

while i != 0:
    item = my_list.pop(0)
    print(item, '-', type(item))
    i -= 1
