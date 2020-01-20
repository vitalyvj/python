r = open('file5_4.txt')
w = open('file5_4_1.txt', 'w', encoding='utf-8')

for i in r.readlines():
    words = i.split()
    for el in words:
        if el == 'One':
            words.remove(el)
            words.insert(0, 'Один ')
        elif el == 'Two':
            words.remove(el)
            words.insert(0, 'Два ')
        elif el == 'Three':
            words.remove(el)
            words.insert(0, 'Три ')
        elif el == 'Four':
            words.remove(el)
            words.insert(0, 'Четыре ')
    words.insert(2, ' ')
    words.insert(4, '\n')

    w.writelines(words)

r.close()
w.close()
