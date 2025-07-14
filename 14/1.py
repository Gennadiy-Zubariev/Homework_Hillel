class MyError(Exception):
    pass


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.gender} {self.age}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.gender} {self.age} {self.record_book}'


class Group:

    def __init__(self, number):
        """

        :rtype: None
        """
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise MyError('My Error')
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.discard(student)

    def find_student(self, last_name):
        for stud in self.group:
            if stud.last_name == last_name:
                return stud

    def __str__(self):
        all_students = ''
        for stud in self.group:
            all_students += f'{stud}\n'
        return f'Number:{self.number}\n {all_students} '


"""Перевірка"""
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 31, 'Steve', 'Jobs', 'AN142')
st4 = Student('Female', 26, 'Liza', 'Taylor', 'AN145')
st5 = Student('Male', 32, 'Steve', 'Jobs', 'AN142')
st6 = Student('Female', 27, 'Liza', 'Taylor', 'AN145')
st7 = Student('Male', 33, 'Steve', 'Jobs', 'AN142')
st8 = Student('Female', 28, 'Liza', 'Taylor', 'AN145')
st9 = Student('Male', 34, 'Steve', 'Jobs', 'AN142')
st10 = Student('Female', 29, 'Liza', 'Taylor', 'AN145')
st11 = Student('Male', 40, 'Steve', 'Jobs', 'AN142')
group = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]
first_super_group = Group(777)
for i in group:
    try:
        first_super_group.add_student(i)
    except MyError:
        print('MyError find')
print(len(first_super_group.group))
