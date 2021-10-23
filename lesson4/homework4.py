from functools import reduce
from itertools import count, cycle
from sys import argv
from random import randrange


"""
Номер 1
"""
name, hours, money_in_hour, prize = argv
salary = int(money_in_hour) * int(hours) + int(prize)
print(salary)


def num2(i=0):
    new_list = []
    len_list = randrange(20)
    my_gen = [randrange(20) for i in range(len_list)]
    print(my_gen)
    try:
        while i != (len_list - 1):
            if my_gen[i] < my_gen[i + 1]:
                new_list.append(my_gen[i + 1])
            i += 1
    except IndexError:
        print(new_list)
    else:
        print(new_list)


def num3():
    gen = (i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0)
    return gen


def num4():
    len_gen = randrange(20)
    gen = [randrange(20) for i in range(len_gen)]
    print(gen)
    new_gen = [el for el in gen if gen.count(el) == 1]
    return new_gen


def num5():
    gen = [i for i in range(100, 1001) if i%2 == 0]
    print(gen)
    return reduce(lambda a, b: a * b, gen)


def num6_1(a, b, c):
    for i in count(a, b):
        if i >= c:
            break
        yield i


def num6_2(my_list, steps, counter=0):
    for i in cycle(my_list):
        """
        steps*len(my_list) - число шагов в одном обороте "cycle()"
        """
        if counter >= steps*len(my_list):
            break
        yield i
        counter += 1


def num7(n, a=1):
    for i in range(1, n+1):
        a *= i
        yield a


"""
main():
"""
q = ' '
while q != '':
    q = input('Введите номер задания или нажмите ENTER: ')
    if q == '1':
        print(f'Заработная плата: {salary}')
    elif q == '2':
        num2()
    elif q == '3':
        for el in num3():
            print(el)
    elif q == '4':
        print(num4())
    elif q == '5':
        print(num5())
    elif q == '6.1':
        a = int(input('Стартовое число: '))
        b = int(input('Шаг: '))
        c = int(input('Предел: '))
        for el in num6_1(a, b, c):
            print(el)
    elif q == '6.2':
        my_list = []
        el = input('Введите элемент списка или ENTER: ')
        while el != '':
            my_list.append(el)
            el = input('Введите элемент списка или ENTER: ')
        print('Оборот - полное прохождение "cycle()" по аргументу-списку')
        steps = int(input('Введите число оборотов "cycle()": '))
        for el in num6_2(my_list, steps, 0):
            print(el)
    elif q == '7':
        n = int(input('Найти фаториал числа: '))
        for el in num7(n):
            print(el)
