class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ZeroDivisionError('На нуль ділити не можна')
        self.a = a
        self.b = b

    @staticmethod
    def find_common_denominator(self_b, other_b):
        for i in range(1, self_b * other_b + 1):
            if i % self_b == 0 and i % other_b == 0:
                return i

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        if self.b == other.b:
            return Fraction(self.a + other.a, self.b)
        else:
            denominator = Fraction.find_common_denominator(self.b, other.b)
            new_self_a = self.a * (denominator // self.b)
            new_other_a = other.a * (denominator // other.b)
            return Fraction(new_self_a + new_other_a, denominator)

    def __sub__(self, other):
        if self.b == other.b:
            return Fraction(self.a - other.a, self.b)
        else:
            denominator = Fraction.find_common_denominator(self.b, other.b)
            new_self_a = self.a * (denominator // self.b)
            new_other_a = other.a * (denominator // other.b)
            return Fraction(new_self_a - new_other_a, denominator)

    def __eq__(self, other):
        if self.b == other.b:
            return self.a == other.a
        else:
            denominator = Fraction.find_common_denominator(self.b, other.b)
            new_self_a = self.a * (denominator // self.b)
            new_other_a = other.a * (denominator // other.b)
            return new_self_a == new_other_a

    def __gt__(self, other):
        if self.b == other.b:
            return self.a > other.a
        else:
            denominator = Fraction.find_common_denominator(self.b, other.b)
            new_self_a = self.a * (denominator // self.b)
            new_other_a = other.a * (denominator // other.b)
            return new_self_a > new_other_a

    def __lt__(self, other):
        if self.b == other.b:
            return self.a < other.a
        else:
            denominator = Fraction.find_common_denominator(self.b, other.b)
            new_self_a = self.a * (denominator // self.b)
            new_other_a = other.a * (denominator // other.b)
            return new_self_a < new_other_a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6'  # 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6'  # 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
