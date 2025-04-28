class CourseList:
    def __init__(self, courses):
        self.courses = courses

    def __len__(self):
        return len(self.courses)

    def __iter__(self):
        return iter(self.courses)

    def __contains__(self, item):
        return item in self.courses

    def __str__(self):
        return f"Courses: {', '.join(self.courses)}"

    def __add__(self, other):
        return len(self.courses) + other

    def __sub__(self, other):
        return len(self.courses) - other

    def __mul__(self, other):
        return len(self.courses) * other

    def __truediv__(self, other):
        return len(self.courses) / other

    def __pow__(self, other):
        return len(self) ** other

    def __iadd__(self, other):
        if isinstance(other, str):
            self.courses.append(other)
        return self

    def __isub__(self, other):
        if isinstance(other, str):
            self.courses.append(other)
        return self

    def __imul__(self, other):
        self.courses = self.courses * other

    def __itruediv__(self, other):
        self.courses = self.courses[:len(self.courses) // other]
        return self


my_courses = CourseList(["Python", "Math", "English"])

print(len(my_courses))
print("Math" in my_courses)

for c in my_courses:
    print(c)

print(my_courses + 2)

my_courses += "History"
print(len(my_courses))

my_courses -= "English"
print(len(my_courses))
