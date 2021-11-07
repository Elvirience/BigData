class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} + {self.y * 1j}'

    def __add__(self, other):
        return (self.x + other.x) + (self.y + other.y) * 1j

    def __mul__(self, other):
        return (self.x * other.x - self.y * other.y) + (self.x * other.y + other.x * self.y) * 1j

    def __del__(self):
        pass


num1 = ComplexNumber(5, 6)
print(num1)
num2 = ComplexNumber(6, 7)
print(num2)
print(num1 + num2)
print(num1 * num2)
