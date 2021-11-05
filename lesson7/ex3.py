from math import ceil


class Cell:
    def __init__(self, quantity):
        self.quantitiy = quantity

    def __add__(self, other):
        return self.quantitiy + other.quantity

    def __sub__(self, other):
        res = self.quantitiy - other.quantity
        if res >= 0:
            return self.quantitiy - other.quantity
        else:
            return print("Разность количества клеток отрицтельна")

    def __mul__(self, other):
        new_cell = self.quantitiy * other.quantity
        return new_cell

    def __truediv__(self, other):
        new_cell = ceil(self.quantitiy / other.quantity)
        return new_cell

    def make_order(self, row):
        my_matrix = []
        a = self.quantitiy % row
        if a == 0:
            for i in range(self.quantitiy // row):
                my_list = []
                for j in range(row):
                    my_list.append('*')
                my_matrix.append(''.join(my_list))
            return '\n'.join(my_matrix)
        else:
            for i in range(self.quantitiy // row):
                my_list = []
                for j in range(row):
                    my_list.append('*')
                my_matrix.append(''.join(my_list))
            my_list = []
            for el in range(a):
                my_list.append('*')
            my_matrix.append(''.join(my_list))
            return '\n'.join(my_matrix)


a = Cell(40)
print(a.make_order(6))
