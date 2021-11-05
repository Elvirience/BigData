import math


class Matrix:

    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __add__(self, other):
        result_matrix = []
        for k, l in zip(self.my_matrix, other.my_matrix):
            result_list = []
            for m, n in zip(k, l):
                result_list.append(m + n)
            result_matrix.append(result_list)
        return Matrix(result_matrix)

    def __str__(self):
        return str(self.my_matrix)


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
c = a + b
print(c)
