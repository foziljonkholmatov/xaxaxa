class Course:
    def __init__(self, name, level):
        self.name = name
        self.level = level


class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def __call__(self, course):
        self.courses.append(course)

c1 = Course('HTML', 'Beginner')
s = Student('Ali')

s (c1)
for c in s.courses:
    print(c.name, '-', c.level)