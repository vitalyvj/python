my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
sorted_list = sorted(my_list)
except_list = [sorted_list[i] for i in range(1, len(sorted_list)) if sorted_list[i] == sorted_list[i - 1]]
result_list = [el for el in my_list if el not in except_list]

print(my_list)
print(result_list)
