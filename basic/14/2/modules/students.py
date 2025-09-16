from .humans import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.gender} {self.age} {self.record_book}'

    def __eq__(self, other):
        s = f'{self.first_name} {self.last_name}, {self.gender} {self.age} {self.record_book}'
        o = f'{other.first_name} {other.last_name}, {other.gender} {other.age} {other.record_book}'
        return s == o

    def __hash__(self):
        return hash(str(self))
