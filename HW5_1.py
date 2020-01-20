text = input('Введите текст: ')
text_to_file = text

while text != '':
    text = input('Введите текст: ')
    text_to_file = text_to_file + '\n' + text

with open('file5_1.txt', 'w') as f:
    f.write(text_to_file)
