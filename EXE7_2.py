from abc import abstractmethod


class Clothes:
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):

    @property
    def calculation(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    @property
    def calculation(self):
        return self.size * 2 + 0.3


venezia = Coat(44)
barcelona = Coat(46)
milena = Suit(1.7)
veronica = Suit(1.6)
all_cost = venezia.calculation + barcelona.calculation + milena.calculation + veronica.calculation

print(f'Расход ткани на костюм "Milena" составит {round(milena.calculation, 2)} м')
print(f'Расход ткани на пальто "Venezia" составит {round(venezia.calculation, 2)} м')
print(f'Расход ткани на пальто "Barcelona" составит {round(barcelona.calculation, 2)} м')
print(f'Расход ткани на костюм "Veronica"  составит {round(veronica.calculation, 2)} м')
print(f'Общий расход ткани составит: {round(all_cost, 2)}  м')
