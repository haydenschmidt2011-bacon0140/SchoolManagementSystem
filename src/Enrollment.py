from src.Course import Course
from src.Student import Student


class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def display_info(self):
        print(self.student.display_info(), self.course.display_info())


    def __str__(self):
        return f"{self.student.name} enrolled in {self.course}"