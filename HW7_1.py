class Matrix:
    def __init__(self, my_list):
        self.matrix = my_list

    def __str__(self):
        return 'Матрица:\n' + '\n'.join('\t'.join(map(str, el)) for el in self.matrix) + '\n'

    def __add__(self, other):
        return [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]


list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

matrix_1 = Matrix(list_1)
print(matrix_1)

matrix_2 = Matrix(list_2)
print(matrix_2)

matrix_3 = Matrix(matrix_1 + matrix_2)
print(matrix_3)
