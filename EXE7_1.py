class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):

        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):

            su_matrix = [[self.matrix[j][i] + other.matrix[j][i] for i in range(len(self.matrix[0]))] for j in
                         range(len(self.matrix))]

            return Matrix(su_matrix)
        else:
            return 'Некорректный ввод данных. Для реализации сложения матрицы должны быть одной размерности!'

    def __str__(self):
        for i in self.matrix:
            for j in i:
                print(j, end='  ')
            print('\n', end='')
        return ''


matrix_1 = Matrix([[1, 2, 4], [2, 4, 8], [3, 4, 6]])

matrix_2 = Matrix([[3, 4, 5, 0], [4, 5, 6, 0], [5, 6, 7, 0]])

print(matrix_1 + matrix_2)
print(matrix_1)
