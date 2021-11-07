class NumeralException(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __del__(self):
        pass


lst = []
i = input('Введите элемент списка: ')
while i != 'q':
    try:
        if i.isdigit() is True:
            lst.append(int(i))
        else:
            """
            Если не число, то проверяю на float
            Если одно из "if" не сработает, выпадет исключение
            """
            check = i.split('.')
            if len(check) == 2:
                if check[0].isdigit() and check[1].isdigit():
                    lst.append(float(i))
                else:
                    break
            else:
                raise(NumeralException('Вы ввели не число!'))
    except NumeralException as error:
        print(error)
    i = input('Введите элемент списка: ')
print(lst)
