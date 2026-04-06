from src.Person import Person
class Student(Person):
    def __init__(self, id, name, email, grade):
        Person.__init__(self, id, name, email)
        self.grade_level = grade

    def enroll(self, course):
        pass

    def display_info(self):
        print(self.name, self.email, self.grade_level)