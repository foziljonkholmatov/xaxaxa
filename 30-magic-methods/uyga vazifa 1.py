class Student:
    def __init__(self, full_name, age, birthday, gender, courses=None ):
        self.full_name = full_name
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.courses = courses if courses else []

    def __str__(self):
        return f"{self.full_name} ({self.gender}), {self.age} age, Birthday {self.birthday}"

    def __repr__(self):
        return f"Student({self.full_name}, {self.age}, {self.birthday}, {self.gender}, {self.courses} "

    def __len__(self):
        return len(self.courses)

    def __iter__(self):
        return iter(self.courses)

    def __contains__(self, item):
        return item in self.courses

    def __iadd__(self, course):
        if isinstance(course, str):
            self.courses.append(course)
        return self

    def __isub__(self, course):
        if isinstance(course, str) and course in self.courses:
            self.courses.remove(course)
        return self


student1 = Student("Ali Valiyev", 30, "1995-05-28", "Male", ["Math", "English"])

print(student1)
print(repr(student1))
print(len(student1))

for course in student1:
    print(course)
print("Math" in student1)

student1 += "English"
print(student1.courses)
student1 -= "Math"
print(student1.courses)
