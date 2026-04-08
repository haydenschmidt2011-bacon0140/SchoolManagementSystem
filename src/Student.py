from src.Person import Person
class Student(Person):
    def __init__(self, id, name, email, grade):
        super().__init__(id, name, email)
        self.grade = grade

    def enroll(self, course):
        pass

    def display_info(self):
        print(self.name, self.email, self.grade_level)

    def __str__(self):
        return f"Student(ID: {self.id}, Name: {self.name}, Username: {self.email}, Grade: {self.grade})"