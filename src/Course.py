class Course:
    def __init__(self, ID, name, teacher):
        self.course_id = ID
        self.course_name = name
        self.teacher = teacher

    def display_info(self):
        print(self.course_id, self.course_name, self.teacher)

    def __str__(self):
        return f"Course(ID: {self.course_id}, Name: {self.course_name}, Instructor: {self.teacher})"