from datetime import date


class Data:

    def __init__(self, data):
        self.data = data

    @classmethod
    def transformer(cls, data):
        lst = data.split('-')
        new_lst = [int(i) for i in lst]
        return cls(new_lst)

    @property
    def your_data(self):
        return print(f'Вы ввели: {self.data}')

    @staticmethod
    def validity(month, year):
        if 1 <= month <= 12:
            pass
        else:
            print('Неправильный месяц')
        if year != date.today().year:
            print('Неактуальный год')

    def __del__(self):
        print('Деструктор сработал')


Data.validity(7, 2025)
b = Data.transformer('12-13-2021')
b.your_data
print(type(b.data))
