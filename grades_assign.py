def assign_grades_for_student(facilitator, student_email, course_code, grades):
    if not hasattr(facilitator, "email") or not facilitator.email:
        print("Invalid email")
        return

    try:
        with open("student.txt", "r") as student_file:
            student_emails = [line.strip().split(",")[1].lower() for line in student_file if "," in line]
    except FileNotFoundError:
        print("Student file not found")
        return

    if student_email.lower() not in student_emails:
        print("Student not found")
        return


    try:
        with open("courses.txt", "r") as course_file:  # fix typo from 'course.txt'
            course_codes = [line.strip().split("/")[-1].upper() for line in course_file if "/" in line]
    except FileNotFoundError:
        print("Course file not found")
        return

    if course_code.upper() not in course_codes:
        print("Course not found")
        return

    possible_grades = {"A", "B", "C", "D", "E", "F"}
    if not (isinstance(grades, str) and grades.upper() in possible_grades):
        print("Invalid grade. Possible grades are: A, B, C, D, E, F.")
        return


    with open("grades.txt", "a") as grades_file:
        grades_file.write(f"{student_email},{course_code.upper()},{grades.upper()}\n")
        print(f"Grade {grades.upper()} assigned to {student_email} for course {course_code.upper()}")
