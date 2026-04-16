class Course:

    def __init__(self, name, students, period, grade, course_type):
        self.name = name
        self.students= students
        self.period = period
        self.grade = grade
        self.course_type = course_type

    def course_description(self):
        print(f"{self.name} a grade {self.grade} {self.course_type} course which happens during period {self.period}. {len(self.students)} students are enrolled")

    def add_student(self, new_stud):
        self.students.append(new_stud)

#_init_(self, name, students, period, grade, course_type)
compsci = Course("Computer Science",["Marcus", "Amish", "Eyal", "Olivia"], 1, 11, "University")
print(compsci.grade)
compsci.numstudents = 23
print(compsci.numstudents)

functions = Course("MCR3U",["Billy", "Kais", "Jonathan", "Agustin"], 3, 11, "University Preparation")
compsci.course_description()
functions.course_description()
#compsci = Course("ICS3U1", ["Billy","Kais","Jonathan", "Agustin"], 3, 11, "University Preparation")
compsci.course_description()
compsci.add_student("Logan")
print(compsci.add_student)
