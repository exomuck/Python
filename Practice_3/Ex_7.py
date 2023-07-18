def sort_students(students):
    sorted_students = sorted(students, key=lambda x: (x[1], x[0]))
    return sorted_students