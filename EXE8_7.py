class Complex:
    def __init__(self, num):
        self.a = num.real
        self.b = num.imag

    def __add__(self, other):
        return complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


num_1 = Complex(5 + 6j)
num_2 = Complex(3 - 2j)

print(num_1 + num_2)
print(num_1 * num_2)
