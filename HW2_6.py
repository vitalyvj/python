q = int(input('Введите количество видов товаров: '))
name = []
price = []
quantity = []
unit = []

i = 1
while i <= q:
    name.append(input(f'Введите название {i} товара: '))
    price.append(int(input(f'Введите цену {i} товара: ')))
    quantity.append(int(input(f'Введите количество {i} товара: ')))
    unit.append(input(f'Введите единицу измерения {i} товара: '))
    goods = {'название': name, 'цена': price, 'количество': quantity, 'ед.': unit}
    goods_list = (i, goods)
    print(goods_list)
    i += 1

for good in goods.items():
    print(good)
