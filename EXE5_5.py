class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Рисуем ручкой'


class Pencil(Stationery):
    def draw(self):
        return 'Рисуем карандашем'


class Handle(Stationery):
    def draw(self):
        return 'Рисуем маркером'


draw_1 = Handle('Рисунок')
print(draw_1.title)
print(draw_1.draw())
