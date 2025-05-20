import os
import unittest

from grades_assign import *
from Student_Course_Management import Users, Student, Facilitator
from register_and_login import user_registration, user_login
from Enroll_student import student_enrollment
from viewing_Grades import viewing_grades


class TestStudentCourse(unittest.TestCase):
    def setUp(self):
        self.Student = Student("Jide", "Jide@gmail.com", "passwordJide")
        self.Facilitator = Facilitator("Sk", "sk@gmail.com", "passwordSk")

        with open("student.txt", "w") as file:
            file.write("Jide,Jide@gmail.com,passwordJide\n")

        with open("facilitator.txt", "w") as file:
            file.write("Sk,sk@gmail.com,passwordSk\n")

        with open("courses.txt", "w") as file:
            file.write("PYTHON/PY01\n")
            file.write("JAVA/Java02\n")

        with open("grades.txt", "w") as file:
            file.write("jide@gmail.com,PY01,A\n")
            file.write("jide@gmail.com,JAVA02,B\n")
            file.write("other@example.com,JS01,C\n")




        open("grades.txt", "w").close()

    def tearDown(self):
        os.remove("student.txt")
        os.remove("facilitator.txt")
        os.remove("grades.txt")
        os.remove("courses.txt")

    def test_user_registration_Student(self):
        expected = user_registration("student", "TestUser", "testuser@gmail.com", "test123")
        self.assertIsInstance(expected, Student)

    def test_user_registration_facilitator(self):
        expected = user_registration("facilitator", "Teach", "teach@gmail.com", "teach123")
        self.assertIsInstance(expected, Facilitator)

    def test_user_registration_is_not_duplicate(self):
        user_registration("student", "Jide", "Jide@gmail.com", "passwordJide")
        result = user_registration("student", "Jide", "Jide@gmail.com", "passwordJide")
        self.assertIsNone(result)

    def test_user_login_successful(self):
        user_registration("student", "Ade", "Ade@gmail.com", "Adepass")
        expected = user_login("Ade@gmail.com", "Adepass")
        self.assertIsInstance(expected, Users)

    def test_user_login_failure(self):
        expected = user_login("Praise@gmail.com", "PraiseFakePassword")
        self.assertIsNone(expected)

    def test_if_course_enroll_is_valid(self):
        student_enrollment(self.Student, "PY01")
        self.assertIn("PYTHON", self.Student.enrolled_courses)
    def test_if_course_is_invalid(self):
        expected = student_enrollment(self.Student, "JS02")
        self.assertIsNone(expected)
        self.assertNotIn("JAVAsCRIPT", self.Student.enrolled_courses)

    def test_assigning_grades_successfully(self):
        assign_grades_for_student(self.Facilitator, "Jide@gmail.com", "PY01", "A")
        with open("grades.txt", "r") as file:
            content = file.read().strip()
        self.assertEqual(content, "Jide@gmail.com,PY01,A")
    def test_assigning_grades_failed(self):
        assign_grades_for_student(self.Facilitator, "JS02", "PY01", "G")
        with open("grades.txt", "r") as file:
            content = file.read().strip()
        self.assertNotIn("Jide@gmail.com,PY01,G",content)

    def test_viewing_grades(self):
        with open("grades.txt", "w") as file:
            file.write("jide@gmail.com,PY01,A\n")
            file.write("jide@gmail.com,JAVA02,B\n")

        results = viewing_grades("jide@gmail.com")
        self.assertIn(("PY01", "A"), results)
        self.assertIn(("JAVA02", "B"), results)



if __name__ == '__main__':
    unittest.main()
