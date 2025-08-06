import random


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def get_square(self):
        return self.width * self.height

    def find_rectangle_sides(self, square):
        res = []
        for i in range(1, square + 1):
            if square % i == 0:
                a = i
                b = square // i
                res.append((a, b))
        return random.choice(res)

    def __eq__(self, other):
        return self.get_square == other.get_square

    def __add__(self, other):
        res = self.get_square + other.get_square
        return Rectangle(*self.find_rectangle_sides(res))

    def __mul__(self, n):
        res = self.get_square * n
        return Rectangle(*self.find_rectangle_sides(res))

    def __str__(self):
        return (f'Прямокутник зі сторонами {self.width} та {self.height}\n'
                f'Площа якого дорівнює {self.get_square}')


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square == 8, 'Test1'
assert r2.get_square == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
