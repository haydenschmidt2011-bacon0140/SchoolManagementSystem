class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def display_info(self):
        print(self.student, self.course)