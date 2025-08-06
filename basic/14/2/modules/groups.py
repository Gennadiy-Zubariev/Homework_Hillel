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
