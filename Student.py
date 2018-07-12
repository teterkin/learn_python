class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def print(self):
        print("--- " + self.name)
        print("Name: " + self.name)
        print("Major: " + self.major)
        print("GPA: " + str(self.gpa))
        print("On probation: " + str(self.is_on_probation))

    def is_on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
