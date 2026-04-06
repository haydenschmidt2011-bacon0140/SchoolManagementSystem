class Course:
    def __init__(self, ID, name, teacher):
        self.course_id = ID
        self.course_name = name
        self.teacher = teacher

    def display_info(self):
        print(self.course_id, self.course_name, self.teacher)