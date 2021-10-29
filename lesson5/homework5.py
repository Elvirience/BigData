"""
Агеев Георгий BigData 1795
"""


import json


def num1():
    fin = open('ex1.txt', 'w', encoding='UTF-8')
    data = input('Введите данные для записи в файл или пустую строку: ')
    while data != '':
        fin.write(data + '\n')
        data = input('Введите данные для записи в файл или пустую строку: ')
    fin.close()


def num2(lines=0, words=0):
    fout = open('ex2.txt', encoding='UTF-8')
    for i in fout.readlines():
        print(f"Число слов в строке {lines + 1}: {len(i.split())}")
        lines += 1
    print(f'Число строк: {lines}')
    fout.close()


def num3(i=0, count=0):
    with open('ex3.txt', encoding='UTF-8') as fout:
        for line in fout:
            surname, salary = line.split()
            i += int(salary)
            if int(salary) < 20000:
                print(surname)
            count += 1
        print(f'Средняя величина дохода: {int(i / count)}')


def num4(i=0):
    fout = open('ex4.txt', encoding='UTF-8')
    fin = open('ex4_in.txt', 'w', encoding='UTF-8')
    my_list = ['Один', 'Два', 'Три', 'Четыре']
    for line in fout:
        line = line.split(' - ')
        line[0] = my_list[i]
        fin.write(' - '.join(line))
        i += 1
    fout.close()
    fin.close()


def num5(i=0, sum=0):
    with open('ex5.txt', 'w+', encoding='UTF - 8') as fin:
        fin.write('5 0 1 2 3 7 9 5 6 81 4 56 1')
        fin.seek(0)
        for i in fin.readline().split():
            sum += int(i)
        print(sum)


"""
Успел сделать топорный вариант в рамках заполнения файла, как в примере.
В адекватном решении использовал бы read() + seek()
 для чтения файловой строки поэлементно. 
Если за попавшимся int тоже следует int, 
 то конкотенирую строковые числа и если далее следует не цифра, то делаю их интом int(str+str)
"""


def num6(result_dict={}):
    with open('ex6.txt', encoding='UTF-8') as fout:
        for line in fout:
            line = line.split()
            sum = 0
            """
            Разбил строку на слова без пробелов
            """
            for i in line:
                """
                Каждое слово делю на две части по "("
                Для названия предмета, которое всегда стоит первым элементом в списке,
                 а так же для случаев, когда стоит прочерк, описываю try - except:
                """
                try:
                    i = i.split('(')
                    sum += int(i[0])
                except ValueError:
                    pass
                """
                line[0] - первый элемент каждой строки в файле - название предмета
                После названия предмета следует ":", поэтому делаю срез строки
                """
            unit_dict = {line[0][:-1]: {sum}}
            result_dict.update(unit_dict)
        print(result_dict)


def num7(all_profit=0, count=0, firm_dict={}):
    with open('ex7.txt', encoding='UTF - 8') as fout:
        for line in fout:
            line = line.split()
            profit = int(line[2]) - int(line[3])
            if profit > 0:
                all_profit += profit
            else:
                pass
            count += 1
            unit_dict = {line[0]: profit}
            firm_dict.update(unit_dict)
        my_list = [firm_dict, {'Average profit': all_profit / count}]
        print(my_list)
    """
    json
    """
    with open('ex7.json', 'w', encoding='UTF - 8') as fin:
        fin.write(json.dumps(my_list))


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
    elif q == '7':
        num7()
