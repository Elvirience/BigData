"""
Выполнил: Агеев Георгий (BigData 1795)
"""
"""
Индекс в названии функции соответствует номеру задания
"""
"""
Для демонстрации работы функций следуйте инструкции после запуска программы
"""


def num1():
    my_list = []
    type_list = []
    el = input('Введите элемент списка: ')
    while el != '':
        my_list.append(el)
        if el.isdigit() is True:
            el = int(el)
            """
            Если не int, то str либо и есть str, либо float, либо содержит признаки обоих типов
            """
        else:
            """
            Проверим str на соответсвие float
            str является float, если выполняются три признака
            Плавающая точка - первый признак типа float,
            Второй - она только одна
            """
            check = el.split('.')
            """
            Точка делит строку на две части, тогда длина списка "check" должна быть строго равна 2
            Если это не так, то тип данных str
            """
            if len(check) == 2:
                """
                # Третий признак - обе части списка должны состоять только из цифр
                # Если это не так, то тип данных str
                """
                if check[0].isdigit() and check[1].isdigit():
                    el = float(el)
                else:
                    break
            else:
                el = str(el)
        type_list.append(type(el))
        el = input('Введите элемент списка: ')
    print(f'Исходный список: {my_list}')
    print(f'Типовой список: {type_list}')


def num2():
    my_list = []
    el = input('Введите элемент списка: ')
    while el != '':
        my_list.append(el)
        el = input('Введите элемент списка: ')
    print(f'Исходный список: {my_list}')
    i = 0
    while i < len(my_list):
        if i is (len(my_list) - 1) and len(my_list) / 2 is not int:
            break
        """
        вариант через кортеж:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        i += 2
        """
        a = my_list[i]
        i += 1
        my_list[i - 1] = my_list[i]
        my_list[i] = a
        i += 1
    print(f'Результат: {my_list}')


def num3():
    do = ''
    while do != '3':
        do = input('Что использовать?\n1.Словарь\t2.Список\t3.Выход\n')
        """
        Решение с помощью словаря
        """
        if do == '1':
            my_dict = {1: 'Jan', 2: 'Feb', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug', 9: 'Sept',
                       10: 'Oct', 11: 'Nov', 12: 'Dec'}
            key = int(input('Введите номер месяца: '))
            if my_dict.get(key) == 12 or 1 or 2:
                print(f'{my_dict.get(key)}, время года года - зима')
            elif my_dict.get(key) == 3 or 4 or 5:
                print(f'{my_dict.get(key)}, время года года - весна')
            elif my_dict.get(key) == 6 or 7 or 8:
                print(f'{my_dict.get(key)}, время года года - лето')
            elif my_dict.get(key) == 9 or 10 or 11:
                print(f'{my_dict.get(key)}, время года года - осень')
            else:
                print('Некорректный ввод')
            """
            Решение с помощью списка
            """
        elif do == '2':
            four_seasons = ['Зима', 'Весна', 'Лето', 'Осень']
            key = int(input('Введите номер месяца: '))
            try:
                print(four_seasons[key // 3])
            except IndexError:
                print('Зима')


def num4():
    string = input('Введите строку: ')
    my_list = string.split(' ')
    for i in my_list:
        print(f'{my_list.index(i) + 1}) {i[0:10]}')


def num5():
    my_list = [5, 5, 10, 4, 1, 4, 4, 6, 2, 6, 10, 7]
    my_list.sort()
    el = input('Введите элемент списка: ')
    while el != '':
        el = int(el)
        try:
            pos = my_list.index(el)
        except ValueError:
            my_list.append(el)
            my_list.sort()
        else:
            my_list.insert(pos, el)
        el = input('Введите элемент списка: ')
    print(my_list)
    my_list.reverse()
    print(f'Рейтинговый список:\n{my_list}')


"""
"condition" - это функция для условия "if" в заданнии 6.
Она проходит по списку, элементами которого являются кортежи вида: (индекс, словарь),
запрашивает j-ый элемент списка, 1-ый элемент кортежа и переходит таким образом к работе со словарем.
Функцией "my_dict.setdefault(nom))" запрашивает значение, находящееся под ключ-переменной "nom"
и добавляет его в список значений "values".
Полученный список ("values") становится значением нового, локального, словаря "my_dict_local"
с ключом "nom".

В результате работы данной функции получаются словари следующего вида:
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
"""


def condition(j, my_list, values, nom):
    while j < len(my_list):
        values.append(my_list[j][1].setdefault(nom))
        j += 1
    my_dict_local = {nom: values}
    print(my_dict_local)


def num6():
    my_list = []
    i = 0
    do = ''
    print('Выберите действие:')
    while do != '3':
        do = input('1.Добавить товар\t2.Выборка\t3.Выход\n')
        if do == '1':
            name = input('Наименование: ')
            price = input('Цена: ')
            quantity = input('Количество: ')
            unit = input('Единица измерения: ')
            my_dict = {'Наименование': name, 'Цена': price, 'Количество': quantity, 'ед.': unit}
            my_tuple = (i + 1, my_dict)
            i += 1
            my_list.append(my_tuple)
        elif do == '2':
            values = []
            j = 0
            do = input('1.Наименование\n2.Цена\n3.Количество\n4.ед.\n')
            if do == '1':
                condition(j, my_list, values, 'Наименование')
            elif do == '2':
                condition(j, my_list, values, 'Цена')
            elif do == '3':
                condition(j, my_list, values, 'Количество.')
            elif do == '4':
                condition(j, my_list, values, 'ед.')


"""
main():
"""
q = ' '
while q != '':
    q = input('Введите номер задания или нажмите ENTER: ')
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
