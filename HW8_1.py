class Data:
    def __init__(self, string=input('Введите дату в формате DD-MM-YYYY: ')):
        self.string = string
        global date, month, year
        date = self.string.split('-')[0]
        month = self.string.split('-')[1]
        year = self.string.split('-')[2]

    @classmethod
    def conversion(cls):
        Data().__init__()
        try:
            int_date = int(date)
            int_month = int(month)
            int_year = int(year)
        except ValueError:
            print("Введен неверный формат даты")
            raise SystemExit

    @staticmethod
    def validation():
        if len(date) != 2 or len(month) != 2 or len(year) != 4 or int(date) > 31 or int(month) > 12:
            print('Введен неверный формат даты')
        else:
            print(f'Число {date}\nМесяц {month}\nГод {year}')


Data.conversion()
Data.validation()
