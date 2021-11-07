class MyExcept(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __del__(self):
        pass


try:
    a = int(input('Числитель: '))
    b = int(input('Знаменатель: '))
    if b == 0:
        raise MyExcept('Деление на ноль!')
    res = a/b
except MyExcept as error:
    print(error)
else:
    print(f'Ответ: {res}')
