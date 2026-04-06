from src.Student import Student
from src.Staff import Staff
from src.Course import Course
from src.Enrollment import Enrollment
from src.System import System

System = System()

Hayden = Student(1, "Hayden", "haschmidt", 9)
Brayden = Student(2, "Brayden", "bschmidt", 9)
System.add_student("Hayden")
System.add_student("Brayden")
HaydenEnroll = Enrollment("Hayden", "Geometry")
BraydenEnroll = Enrollment("Brayden", "Python")
System.add_enrollment("Hayden", "Geometry")
System.add_enrollment("Brayden", "Python")

Omar = Staff(11, "Omar", "omaralk", "Python")
Brunkan = Staff(12, "Brunkan", "mrbrunkan", "Geometry")
System.add_staff("Omar")
System.add_staff("Brunkan")

Python = Course(21, "Python", "Omar")
Geometry = Course(22, "Geometry", "Brunkan")
System.add_course("Python")
System.add_course("Geometry")

print(System.display_student_enrollments(0, "Hayden"))
print(System.display_student_enrollments(1, "Brayden"))
print(System.list_staff())
print(System.list_courses())
print(System.list_students())

# I created a video showing the problem, and sent it via gmail