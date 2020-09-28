class Cell:

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return f'Общая клетка после сложения имеет {self.cell + other.cell} ячеек'

    def __sub__(self, other):
        new_cell = abs(self.cell - other.cell)
        if new_cell > 0:
            return f'Общая клетка после вычитания имеет {new_cell} ячеек'
        else:
            return 'Клетки имеют одинаковое количество ячеек'

    def __mul__(self, other):

        return f'Общая клетка после умножения имеет {self.cell * other.cell} ячеек'

    def __truediv__(self, other):
        new_cell = self.cell // other.cell if self.cell > other.cell else other.cell // self.cell
        return f'Общая клетка после деления имеет {new_cell} ячеек'

    def make_order(self, num_one):
        i = 0
        while i < self.cell:
            for j in range(num_one):
                if i < self.cell:
                    print('*', end='')
                    i += 1
            print('\n', end='')


cell_1 = Cell(12)
cell_2 = Cell(16)
cell_3 = Cell(27)
cell_1.make_order(5)
cell_3.make_order(8)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
