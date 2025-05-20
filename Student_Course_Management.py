

class Users:
    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password

class Student(Users):
    def __init__(self, full_name, email, password):
        super().__init__(full_name,email,password)
        self.enrolled_courses = []

class Facilitator(Users):
    def __init__(self, full_name, email, password):
        super().__init__(full_name,email,password)
        self.created_courses = None
        self.Courses_created = []

class Course(Users):
    def __init__(self, course_name, course_code, facilitator):
        self.Course_name = course_name
        self.course_code = course_code
        self.Facilitator = facilitator
        self.Student_that_enrolled = []
        self.grades = []

