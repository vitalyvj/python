with open('file5_2.txt') as f:
    strings = f.readlines()

    i = 1
    for el in strings:
        words = len(el.split())
        if words == 1:
            print(f'В {i} строке {words} слово')
        elif words < 5:
            print(f'В {i} строке {words} слова')
        else:
            print(f'В {i} строке {words} слов')
        i += 1

print(f'Всего в файле {i - 1} строк')
