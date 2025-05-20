from Student_Course_Management import Student, Facilitator, Course
from grades_assign import assign_grades_for_student
from register_and_login import user_registration,user_login
from viewing_Grades import viewing_grades


def main():
    print("\nWelcome to the Student Management System!")
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            user_type = input("Register as (student/facilitator: ").lower()
            if user_type in ["student", "facilitator"]:
                user_registration(user_type)
            else:
                print("Invalid role. Try again.")

        elif choice == "2":
            user = user_login()
            if user:
                user_dashboard(user)

        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


def user_dashboard(user):
    """Handles student/instructor actions after login"""
    print(f"\nWelcome, {user.name}!")
    if isinstance(user, Student):
        while True:
            print("\nStudent Menu:")
            print("1. View Courses")
            print("2. View Grades")
            print("3. Logout")

            choice = input("Enter choice: ")
            if choice == "1":
                print(f"Enrolled Courses: {user.enrolled_courses}")
            elif choice == "2":
                viewing_grades(user.email)
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Try again.")

    elif isinstance(user, Facilitator):
        while True:
            print("\nInstructor Menu:")
            print("1. Create Course")
            print("2. Assign Grade")
            print("3. Logout")

            choice = input("Enter choice: ")
            if choice == "1":
                course_name = input("Enter course name: ")
                course_code = input("Enter course code: ")
                new_course = Course(course_name, course_code, user)
                user.created_courses.append(new_course)
                print(f"Course {course_name} created successfully!")
            elif choice == "2":
                student_email = input("Enter student email: ")
                course_code = input("Enter course code: ")
                grade = input("Enter grade: ")
                assign_grades_for_student(user, student_email, course_code, grade)
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()