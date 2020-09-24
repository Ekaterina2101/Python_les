class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._weight_one = 25
        self._thickness = 5

    def weight(self):
        return self._length * self._width * self._thickness * self._weight_one / 1000


instance = Road(20, 5000)
print(f'{instance.weight()} тонн асфалта потребуется для покрытия дорожного полотна')
