class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return float(self._income.get('wage')) + float(self._income.get('bonus'))


posit_1 = Position("Victor", 'Pelevin', 'manager', 3000, 1000)
print(posit_1.get_full_name())
print(posit_1.get_total_income())
