from functools import reduce

my_list = [el for el in range(100, 1000 + 1) if el % 2 == 0]
my_func = reduce(lambda x, y: x * y, my_list)

print(my_func)
