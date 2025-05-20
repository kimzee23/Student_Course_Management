def student_enrollment(student, course_code):
    with open("courses.txt", "r") as courseFile:
        courses = courseFile.readlines()

        for course in courses:
            details = course.strip().split("/")  # Fixed separator

            if len(details) < 2:
                print(f"Error: Malformed course entry '{course.strip()}' in file.")
                continue

            if details[1].strip().upper() == course_code.strip().upper():
                student.enrolled_courses.append(details[0])
                print(f"Enrolled in {details[0]}")
                return

        print("Course not found")
        return None
