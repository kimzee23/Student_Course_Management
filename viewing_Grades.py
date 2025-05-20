def viewing_grades(student_email):
    results = []
    try:
        with open('grades.txt', 'r') as grade_file:
            for grade in grade_file:
                details = grade.strip().split(',')
                if len(details) == 3 and details[0].lower() == student_email.lower():
                    results.append((details[1], details[2]))
    except FileNotFoundError:
        return []

    return results