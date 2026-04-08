class System:
    def __init__(self):
        self.students = []
        self.staff = []
        self.courses = []
        self.enroll = {}

    def add_student(self, x):
        self.students.append(x)

    def add_staff(self, x):
        self.staff.append(x)

    def add_course(self, x):
        self.courses.append(x)

    def add_enrollment(self, student, course, teacher):
        self.enroll[student] = (course, teacher)

    def list_students(self):
        for x in self.students:
            print(x)

    def list_staff(self):
        for x in self.staff:
            print(str(x))

    def list_courses(self):
        for x in self.courses:
            print(str(x))

    def display_student_enrollments(self):
        for student, (course, teacher) in self.enroll.items():
            print(student, "Is Enrolled In", course, "With", teacher.email)