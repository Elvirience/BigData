"""
Выполнил: Агеев Георгий (BigData 1795)
"""
"""
Индекс в названии функции соответствует номеру задания
"""
"""
Для демонстрации работы функций следуйте инструкции после запуска программы
"""
"""
ВНИМАНИЕ!
Для 6-го задания предусмотрены варианты ввода: 6.1 - для обратоки слова, 6.2 - для обработки нескольких слов
"""


def num1(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Деление на 0')
        print('Попробуте еще раз!')
        a = int(input('Числитель = '))
        b = int(input('Знаменатель = '))
        print(a / b)
    return a/b


def num2(name, nom, born, city, email, number):
    print(f'Имя: {name}\tФамилия: {nom}\tГод рождения: {born}\tГород: {city}\te-mail: {email}\tТелефон: {number}\n')


def num3(a, b, c, j):
    my_list = [a, b, c]
    """
    Определяю тип переменной: int или float
    """
    for i in my_list:
        if i.isdigit() is True:
            i = int(i)
        else:
            check = i.split('.')
            if len(check) == 2:
                if check[0].isdigit() and check[1].isdigit():
                    i = float(i)
        my_list[j] = i
        j += 1
    """
    Цикл на случай, если решение требует не использовать функцию ".sort()"
    """
    """
    j = 0
    while j < 2:
         if my_list[j] > my_list[j + 1]:
            my_list[j + 1] = my_list[j]
         else:
            j += 1
         j += 1
    """
    my_list.sort()
    print(my_list[1] + my_list[2])
    return my_list[1] + my_list[2]


def num4(x, y):
    for i in range(abs(y)):
        x *= x
    print(1 / x)
    return 1 / x


def num5(string, sum, j):
    """
    Суммирование вводимых чисел до того, как попадется специальный символ "q"
    """
    while string.count('q') == 0:
        my_list = string.split(' ')
        for i in my_list:
            sum += int(i)
        print(sum)
        string = input('Введите числа через пробел: ')
        string.count('q')
    """
    Как только строка содержит специальный символ, происходит суммирование чисел перед ним - работа завершается
    """
    my_list = string.split(' ')
    while my_list[j] != 'q':
        sum += int(my_list[j])
        j += 1
    print(sum)


"""
Вспомогательная функция к заданию "6", обрататывающая, по заданию, одно слово
"""


def helper(my_string, i):
    alphabet = (('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'),
                ('f', 'F'), ('g', 'G'), ('h', 'H'), ('i', 'I'), ('j', 'J'),
                ('k', 'K'), ('l', 'L'), ('m', 'M'), ('n', 'N'), ('o', 'O'),
                ('p', 'P'), ('q', 'Q'), ('r', 'R'), ('s', 'S'), ('t', 'T'),
                ('u', 'U'), ('v', 'V'), ('w', 'W'), ('x', 'X'), ('y', 'Y'), ('z', 'Z'))
    while my_string[0] != alphabet[i][0]:
        i += 1
    print(alphabet[i][1] + my_string[1:])
    return alphabet[i][1] + my_string[1:]


"""
Здание 6.2. Например, вы ввели: aleksandra shapovalova
                   Результат: Aleksandra
                              Shapovalova
                              Aleksandra Shapovalova
        Первые две строки отображаются в результате работы функции "helper"
"""


def num6(string):
    """
    Список, чтобы собрать функцкцией .join()
    """
    my_list = []
    """
    Работа функции "helper" над каждым словом строки, введенной пользователем
    """
    for j in string.split(' '):
        my_list.append(helper(j, 0))
    """
    Сброка получившегося списка в строку
    """
    print(' '.join(my_list))
    return ' '.join(my_list)


"""
main():
"""
q = ' '
while q != '':
    q = input('Введите номер задания или нажмите ENTER: ')
    if q == '1':
        a = int(input('Числитель = '))
        b = int(input('Знаменатель = '))
        num1(a, b)
    elif q == '2':
        name = input('Имя: ')
        nom = input('Фамилия: ')
        born = input('Год рождения: ')
        city = input('Город: ')
        email = input('e-mail: ')
        number = input('Телефон: ')
        num2(name, nom, born, city, email, number)
    elif q == '3':
        a = input('a = ')
        b = input('b = ')
        c = input('c = ')
        num3(a, b, c, 0)
    elif q == '4':
        x = abs(float(input('Введите действительное положительное число: ')))
        y = int(input('Введите целое отрицательное число: '))
        num4(x, y)
    elif q == '5':
        string = input('Введите числа через пробел: ')
        num5(string, 0, 0)
    elif q == '6.1':
        my_string = input('Введите слово из маленьких латинских букв: ')
        helper(my_string, 0)
    elif q == '6.2':
        string = input('Введите слова из маленьких латинских букв: ')
        num6(string)
