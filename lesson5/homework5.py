"""
Агеев Георгий BigData 1795
"""
"""
Добавлю 7-ую
"""
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
        print(f'Средняя величина дохода: {int(i/count)}')



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

        
def num6(result_dict={}):
    with open('ex6.txt', encoding='UTF - 8') as fout:
        for line in fout:
            line = line.split()
            sum = 0
            for i in line:
                try:
                    i = i.split('(')
                    sum += int(i[0])
                except ValueError:
                    pass
            unit_dict = {line[0][:-1]: {sum}}
            result_dict.update(unit_dict)
        print(result_dict)

        
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
