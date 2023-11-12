import csv

class Student:
    def __init__(self, name, surname, school_class, year_of_birth, grade_avg):
        self.name = name
        self.surname = surname
        self.school_class = school_class
        self.year_of_birth = year_of_birth
        self.grade_avg = grade_avg

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Class: {self.school_class}," \
                f"Brith: {self.year_of_birth}, Grade: {self.grade_avg}"



    @classmethod
    def from_file(cls, file, class_name=None):
        students = []
        with open(file) as students_file:
            for row in csv.reader(students_file):
                if class_name is None or class_name == row[2]:
                    students.append(
                        cls(row[0], row[1], row[2], int(row[3]), float(row[4]))
                    )
        return students



john = Student('John', 'Smith', '1A', 2012, 4.78)
jane = Student('Jane', 'Adams', '2C', 2011, 5.11)
student_1 = Student.from_file('students.csv')  # ALL students
student_2 = Student.from_file('students.csv', '2A')

print(john)
print(jane)
print(student_1)
print(student_2)