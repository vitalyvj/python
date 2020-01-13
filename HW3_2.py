def my_func(name, surname, year, city, mail, phone):
    print(f'Имя: {name}, фамилия: {surname}, год рождения: {year}, город проживания: {city}, '
          f'e-mail: {mail}, номер телефона: {phone}')


my_func(
    name=input('Введите имя: '),
    surname=input('Введите фамилию: '),
    year=input('Введите год рождения: '),
    city=input('Введите город проживания: '),
    mail=input('Введите e-mail: '),
    phone=input('Введите номер телефона: ')
)
