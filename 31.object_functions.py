from Student import Student

students = [
    Student("Jim","Business", 3.5, False),
    Student("Pam","Art", 2.5, True),
    Student("Kevin","Computer science", 3.5, False)
]


def students_on_honor_roll(students_list):
    print("Students on honor roll:")
    print("-----------------------")
    count = 1
    for student in students_list:
        if student.is_on_honor_roll():
            print(str(count) + ". " + student.name)
            count += 1


students_on_honor_roll(students)
