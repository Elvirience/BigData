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
        my_list = []
        for i in range(row):

