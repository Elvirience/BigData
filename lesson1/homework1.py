"""
Выполнил: Агеев Георгий (AI 1781)
"""
"""
Индекс в названии функции соответствует номеру задания
"""
"""
Для демонстрации работы функций следуйте инструкции после запуска программы
"""


def num1():
    a = None
    b = 1
    c = 1.7
    print(f'a = {a}, b = {b}, c = {c}')
    a = input('a = ')
    b = input('b = ')
    c = input('c = ')
    print(f'a = {a}, b = {b}, c = {c}')


def num2():
    t = int(input(f'Введите время в секундах: '))
    ts = t%60
    tm = int(t/60)%60
    th = int(t/3600)
    print(f'{th}:{tm}:{ts}')


def num3():
    n = input('Введите число: ')
    nn = n+n
    nnn = n+n+n
    a = int(n)
    b = int(nn)
    c = int(nnn)
    print(int(a + b + c))


def num4():
    n = int(input(f'Введите целое положительное число: '))
    var = 0
    while n != 0:
        m = n % 10
        if m > var:
            var = m
        n = n // 10
        print(f'Наибольшая цифра в числе: {var}')


def num5():
    p = int(input('Введите сумму выручки: '))
    c = int(input('Введите сумму издержек: '))
    if p > c:
        print('Фиксируем прибыль')
        print(f'Рентабельность: {(p - c) / p}')
        num = int(input('Введите число работников: '))
        print(f'Прибыль на сотрудника компании составляет: {(p - c) / num}')
    else:
        print('Терпим убытки')


def num6():
    a = float(input('Рекорд: '))
    b = float(input('Цель: '))
    count = 0
    i = 1
    while a <= b:
        print(f'{i}-ый день: {a:.{3}f}')
        a = a + a * 10 / 100
        count += 1
        i += 1
    print(f'Результат {a:.{3}f} км будет достигнут на {count} день')


answer = ''
while answer != 'n':
    answer = input('Начнем? (y/n): ')
    if answer == 'y':
        q = ''
        while q != ' ':
            q = input('Введите номер задания или пробел: ')
            if q == '1':
                num1()
            elif q == '2':
                num2()
            elif q == '3':
                num3()
            elif q == '4':
                num4()
            elif q == '5':
                num5()
            elif q == '6':
                num6()
            else:
                print('Некорректный ввод')
