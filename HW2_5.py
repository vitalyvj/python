my_list = [7, 5, 3, 3, 2]
print(my_list)

new_element = int(input('Введите натуральное число: '))

for i in range(len(my_list)):
    if new_element > my_list[i]:
        my_list.insert(i, new_element)
        break
    elif new_element <= my_list[-1]:
        my_list.insert(len(my_list), new_element)
        break

print(my_list)
