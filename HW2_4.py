string = input('Введите строку из нескольких слов: ')
sep_words = string.split()

for i, word in enumerate(sep_words, start=1):
    print(i, word if len(word) <= 10 else word[:10])
